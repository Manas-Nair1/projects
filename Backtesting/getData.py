import ccxt
import pandas as pd

# Initialize ccxt exchange (you may need to select a specific exchange)
exchange = ccxt.kucoin()  # Replace 'binance' with your desired exchange
start_date = exchange.parse8601('2022-01-01T00:00:00Z')

# Fetch OHLCV data for BTC/USDT
btc_ohlcv = exchange.fetch_ohlcv('BTC/USDT', timeframe='8h', since= start_date, limit=1500)  # Adjust limit as needed

# Fetch OHLCV data for ETH/USDT
eth_ohlcv = exchange.fetch_ohlcv('ETH/USDT', timeframe='8h', since= start_date, limit=1500)  # Adjust limit as needed

# Convert fetched data into pandas DataFrames
btc_df = pd.DataFrame(btc_ohlcv, columns=['timestamp', 'open', 'high', 'low', 'close', 'volume'])
eth_df = pd.DataFrame(eth_ohlcv, columns=['timestamp', 'open', 'high', 'low', 'close', 'volume'])

# Save data to CSV files
btc_df.to_csv('BTC_USDT.csv', index=False)
eth_df.to_csv('ETH_USDT.csv', index=False)


import datetime

timestamp_string = '2023-01-01T00:00:00Z'

# Convert the timestamp string to a datetime object
timestamp_datetime = datetime.datetime.strptime(timestamp_string, '%Y-%m-%dT%H:%M:%SZ')

# Convert the datetime object to a Unix timestamp in seconds
unix_timestamp_seconds = int(timestamp_datetime.timestamp())

print(unix_timestamp_seconds)

import datetime

timestamp_milliseconds = 1684166400000  # Replace this with your timestamp

# Convert milliseconds since the epoch to a datetime object
date_time = datetime.datetime.fromtimestamp(timestamp_milliseconds / 1000.0) 

print(date_time)
