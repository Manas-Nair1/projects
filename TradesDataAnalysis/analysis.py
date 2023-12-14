import pandas as pd
from statsmodels.tsa.stattools import adfuller, kpss


file_path = 'TradesAnalysis/tradeData.csv'  

df = pd.read_csv(file_path)
print(df)

df['timestamp'] = pd.to_datetime(df['timestamp'])
df['side'] = df['side'].map({'sell': -1, 'buy': 1})

df['order_size'] = df['size'] * df['side']

result = adfuller(df['order_size'])

print('ADF Statistic:', result[0])
print('p-value:', result[1])
print('Critical Values:')
for key, value in result[4].items():
    print(f'\t{key}: {value}')

kpss_stat, p_value, lags, critical_values = kpss(df['order_size'])

print(f'KPSS Statistic: {kpss_stat}')
print(f'p-value: {p_value}')
print('Critical Values:')
for key, value in critical_values.items():
    print(f'   {key}: {value}')

