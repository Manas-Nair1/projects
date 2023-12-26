import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("Backtesting/residualRatio.csv")

ratio = df["close"]
# df['zscore']= (ratio - ratio.mean())/ratio.std()
ratios_mavg5 = ratio.rolling(window=5, center=False).mean()
ratios_mavg20 = ratio.rolling(window=20, center=False).mean()
std_20 = ratio.rolling(window=20, center=False).std()
zscore_20_5 = (ratios_mavg5 - ratios_mavg20)/std_20
# print(df)
df["signal"] = zscore_20_5
print(zscore_20_5)
print(df)
df.to_csv("signals.csv")

data = pd.Series(zscore_20_5)

plt.figure(figsize=(10, 6))
plt.plot(data.index, data.values)
plt.xlabel('Index')
plt.ylabel('Value')
plt.title('Plot of Data versus Index')
plt.grid(True)
plt.savefig("zscore.png")
plt.show()