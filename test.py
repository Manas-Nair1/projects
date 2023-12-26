import ccxt
import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm
import statsmodels.tsa.stattools as ts

exchange = ccxt.kucoin()

symbols = ['BTC/USDT', 'ETH/USDT']
def get_data():
    dfs = {}
    for symbol in symbols:
        ohlcv = exchange.fetch_ohlcv(symbol, timeframe='5m', limit=1500)
        filtered_data = ohlcv

        df = pd.DataFrame(filtered_data, columns=['timestamp', 'open', 'high', 'low', 'close', 'volume'])
        df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms')  
        df.set_index('timestamp', inplace=True)
        dfs[symbol] = df


    btc_data = dfs['BTC/USDT']
    eth_data = dfs['ETH/USDT']


    btc_close = btc_data['close'].rename('BTC_Close')  
    eth_close = eth_data['close'].rename('ETH_Close')  

    df = pd.concat([btc_close, eth_close], axis=1)  
    return df


# print(df)
def create_residuals(price_df):

    # Create OLS model
    y = price_df['BTC_Close']
    x = price_df['ETH_Close']
    x = sm.add_constant(x)
    model = sm.OLS(y, x)
    res = model.fit()
    
    # Beta hedge ratio (coefficent from OLS)
    beta_hr = res.params[1]
    # print(f'Beta Hedge Ratio: {beta_hr}')
    
    # Residuals
    price_df["Residuals"] = res.resid
    return price_df
# cadf = ts.adfuller(df["Residuals"])
# print(f'CADF:{cadf}')
def get_signal():
    ratio = df["Residuals"]
    # df['zscore']= (ratio - ratio.mean())/ratio.std()
    ratios_mavg5 = ratio.rolling(window=5, center=False).mean() #used as current value
    ratios_mavg20 = ratio.rolling(window=20, center=False).mean() #used as mean
    std_20 = ratio.rolling(window=20, center=False).std() #used as stdev
    zscore_20_5 = (ratios_mavg5 - ratios_mavg20)/std_20
    # print(df)
    df["signal"] = zscore_20_5
    # print(zscore_20_5)
    # print(df)
# df.to_csv("signals.csv")

    data = pd.Series(zscore_20_5)
    return data

df = get_data()
df = create_residuals(df)
signal = get_signal()
print(signal)




