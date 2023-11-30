import ccxt
import pandas as pd
import matplotlib.pyplot as plt

exchange = ccxt.kucoin()

symbols = ['BTC/USDT', 'ETH/USDT']
start_date = exchange.parse8601('2022-01-01T00:00:00Z')  # Start date: January 1st, 2022
end_date = exchange.parse8601('2023-01-01T00:00:00Z')    # End date: January 1st, 2023

dfs = {}
for symbol in symbols:
    ohlcv = exchange.fetch_ohlcv(symbol, timeframe='1d', since=start_date, limit=1000)
    filtered_data = [data for data in ohlcv if start_date <= data[0] < end_date]

    df = pd.DataFrame(filtered_data, columns=['timestamp', 'open', 'high', 'low', 'close', 'volume'])
    df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms')  # Convert timestamp to datetime
    df.set_index('timestamp', inplace=True)
    dfs[symbol] = df


btc_data = dfs['BTC/USDT']
eth_data = dfs['ETH/USDT']
print(btc_data)

def create_residuals(price_df):
    """
    Calculate the OLS and create the beta hedge ratio and residuals for the two 
    equites XOM and USO.

    Parameters
    ----------
    price_df : `pd.DataFrame`
        A DataFrame containing XOM and USO Adjusted Close data from
        01/01/2019-01/01/2020. Index is a Datetime object.

    Returns
    -------
    price_df : `pd.DataFrame`
        Updated DataFrame with column values for beta hedge ratio (beta_hr) and 
        residuals (Residuals).
    """
    # Create OLS model
    Y = price_df['USO Price($)']
    x = price_df['XOM Price($)']
    x = sm.add_constant(x)
    model = sm.OLS(Y, x)
    res = model.fit()
    
    # Beta hedge ratio (coefficent from OLS)
    beta_hr = res.params[1]
    print(f'Beta Hedge Ratio: {beta_hr}')
    
    # Residuals
    price_df["Residuals"] = res.resid
    return price_df