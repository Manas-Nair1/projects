import ccxt
import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm
import statsmodels.tsa.stattools as ts

exchange = ccxt.kucoin()

symbols = ['BTC/USDT', 'ETH/USDT']
start_date = exchange.parse8601('2018-01-01T00:00:00Z')  # Start date: January 1st, 2018
end_date = exchange.parse8601('2023-10-01T00:00:00Z')    # End date: January 1st, 2023

dfs = {}
for symbol in symbols:
    ohlcv = exchange.fetch_ohlcv(symbol, timeframe='1d', since=start_date)
    filtered_data = [data for data in ohlcv if start_date <= data[0] < end_date]

    df = pd.DataFrame(filtered_data, columns=['timestamp', 'open', 'high', 'low', 'close', 'volume'])
    df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms')  # Convert timestamp to datetime
    df.set_index('timestamp', inplace=True)
    dfs[symbol] = df


btc_data = dfs['BTC/USDT']
eth_data = dfs['ETH/USDT']

btc_close = btc_data['close'].rename('BTC_Close')  # Extract 'close' column for BTC and rename it
eth_close = eth_data['close'].rename('ETH_Close')  # Extract 'close' column for ETH and rename it

df = pd.concat([btc_close, eth_close], axis=1)  # Concatenate both 'close' columns into a single DataFrame

print(df)

def create_residuals(price_df):
   
    # Create OLS model
    Y = price_df['BTC_Close']
    x = price_df['ETH_Close']
    x = sm.add_constant(x)
    model = sm.OLS(Y, x)
    res = model.fit()
    
    # Beta hedge ratio (coefficent from OLS)
    beta_hr = res.params[1]
    print(f'Beta Hedge Ratio: {beta_hr}')
    
    # Residuals
    price_df["Residuals"] = res.resid
    return price_df

print(create_residuals(df))
cadf = ts.adfuller(df["Residuals"])
print(f'CADF:{cadf}')