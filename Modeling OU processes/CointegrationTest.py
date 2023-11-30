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


plt.figure(figsize=(10, 6))
plt.plot(btc_data.index, btc_data['close'], label='BTC/USDT', color='blue')
plt.plot(eth_data.index, eth_data['close'], label='ETH/USDT', color='orange')
plt.xlabel('Date')
plt.ylabel('Price (USDT)')
plt.title('BTC/USDT and ETH/USDT OHLCV')
plt.legend()
plt.grid(True)

relative_difference = eth_data['close'] / btc_data['close']
plt.figure(figsize=(10, 4))
plt.plot(relative_difference.index, relative_difference, label='Relative Difference', color='green')
plt.xlabel('Date')
plt.ylabel('Relative Difference (ETH/BTC)')
plt.title('Relative Difference between ETH/USDT and BTC/USDT')
plt.legend()
plt.grid(True)

plt.savefig('cointegrationTest.png')
plt.show()
