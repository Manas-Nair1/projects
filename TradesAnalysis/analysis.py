import pandas as pd
from statsmodels.tsa.stattools import adfuller

# Your sample trades data (a subset of your full dataset)
data = {
    'timestamp': [
        '2023-10-13 10:00:00', '2023-10-13 10:00:00', '2023-10-13 10:00:00',
        '2023-10-13 10:00:00', '2023-10-13 10:00:00', '2023-10-13 10:00:00',
        '2023-10-13 10:00:00', '2023-10-13 10:00:00', '2023-10-13 10:00:00',
        '2023-10-13 10:00:00', '2023-10-13 10:00:00'
    ],
    'side': ['sell', 'sell', 'sell', 'sell', 'sell', 'sell', 'sell', 'sell', 'sell', 'sell', 'sell'],
    'size': [0.40906938, 0.15618927, 0.16, 0.1469042, 0.13820735, 0.16755721,
             0.14950466, 0.15138358, 0.14861642, 0.1292959, 0.14088824],
    'price': [26854.8, 26847.5, 26847.5, 26847.6, 26847.6, 26847.9,
              26847.3, 26847.3, 26847.3, 26847.3, 26847.2]
}

# Create a DataFrame from the sample data
df = pd.DataFrame(data)

# Convert 'timestamp' column to datetime type
df['timestamp'] = pd.to_datetime(df['timestamp'])

# Perform the ADF test on the 'size' column
result = adfuller(df['size'])

# Extract and print the test results
print('ADF Statistic:', result[0])
print('p-value:', result[1])
print('Critical Values:')
for key, value in result[4].items():
    print(f'\t{key}: {value}')
