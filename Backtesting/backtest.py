import pandas as pd

df = pd.read_csv("Backtesting/signals.csv")
orders = []
for index, row in df.iterrows():
    if row['signal'] > 1:
        # print(row['timestamp'])
        orders.append([row['timestamp'],"short"])
    if row['signal'] < -1:
        # print(row['timestamp'])
        orders.append([row['timestamp'],"long"])

df = pd.DataFrame(orders, columns=['timestamp', 'side'])

# Set the 'timestamp' column as the index
df['timestamp'] = pd.to_datetime(df['timestamp'])  # Convert to datetime if not already
df.set_index('timestamp', inplace=True)

# Rename the columns
df.columns = ['side']
df.to_csv('orders.csv')
# print(df)