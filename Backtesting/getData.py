import ccxt
import pandas as pd

exchange = ccxt.kucoin()  # Replace 'binance' with your desired exchange
start_date = exchange.parse8601('2022-01-01T00:00:00Z')

btc_ohlcv = exchange.fetch_ohlcv('BTC/USDT', timeframe='8h', since= start_date, limit=1500)  # Adjust limit as needed

eth_ohlcv = exchange.fetch_ohlcv('ETH/USDT', timeframe='8h', since= start_date, limit=1500)  # Adjust limit as needed

btc_df = pd.DataFrame(btc_ohlcv, columns=['timestamp', 'open', 'high', 'low', 'close', 'volume'])
eth_df = pd.DataFrame(eth_ohlcv, columns=['timestamp', 'open', 'high', 'low', 'close', 'volume'])

btc_df.to_csv('BTC_USDT.csv', index=False)
eth_df.to_csv('ETH_USDT.csv', index=False)


#checking start and end datetimes

import datetime

timestamp_string = '2023-01-01T00:00:00Z'

timestamp_datetime = datetime.datetime.strptime(timestamp_string, '%Y-%m-%dT%H:%M:%SZ')

unix_timestamp_seconds = int(timestamp_datetime.timestamp())

print(unix_timestamp_seconds)


timestamp_milliseconds = 1684166400000  

date_time = datetime.datetime.fromtimestamp(timestamp_milliseconds / 1000.0) 

print(date_time)
