import pandas as pd
from statsmodels.tsa.stattools import adfuller, kpss
import nolds

file_path = 'TradesAnalysis/tradeData.csv'  

df = pd.read_csv(file_path)


df['timestamp'] = pd.to_datetime(df['timestamp'])
df['side'] = df['side'].map({'sell': -1, 'buy': 1})

df['order_size'] = df['size'] * df['side']
df['running_total'] = df['order_size'].cumsum()
print(df)

hurst = nolds.hurst_rs(df['running_total'].values)
print("Estimated Hurst exponent for 'order_size':", hurst)


