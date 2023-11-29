import pandas as pd
from statsmodels.tsa.arima.model import ARIMA
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
import matplotlib.pyplot as plt

file_path = 'TradesAnalysis/tradeData.csv'  

df = pd.read_csv(file_path)
print(df)

df['timestamp'] = pd.to_datetime(df['timestamp'])
df['side'] = df['side'].map({'sell': -1, 'buy': 1})

df['order_size'] = df['size'] * df['side']

data = pd.Series(df['order_size'])

'''
# Plot ACF and PACF to identify ARMA orders
plot_acf(data)
plt.savefig('acf.png') 
plot_pacf(data)
plt.savefig('pacf.png') 
# plt.show()
# plt.savefig('testFig.png') #have to save as png instead of show as codespace cannot display plot 
pass
'''
# Choose orders (p, q) based on ACF and PACF plots
p = 4  # Replace with your selected autoregressive (AR) order
q = 4 # Replace with your selected moving average (MA) order

# Split data into training and testing sets
train_data = data.iloc[:200]  # Replace with your training data
test_data = data.iloc[200:]   # Replace with your testing data

# Fit ARMA model to training data
model = ARIMA(train_data, order=(p, 0, q))  # Use '0' for integrated term in ARIMA for ARMA
arma_model = model.fit()

# Model diagnostics - Check residuals
residuals = arma_model.resid
plt.plot(residuals)
plt.title('Residuals Plot')
plt.savefig('residuals.png')


# Forecast using the fitted model
forecast = arma_model.forecast(steps=len(test_data))

# Evaluate forecasting performance (e.g., RMSE)
# Replace 'true_values' with your actual true values from the test set
true_values = test_data.to_numpy()
forecast_values = forecast.to_numpy()
rmse = ((true_values - forecast_values) ** 2).mean() ** 0.5
print(f'RMSE: {rmse}')

plt.plot(test_data.index, test_data.values, label='Actual', color='blue')

# Plot forecasted values
plt.plot(test_data.index, forecast, label='Forecast', color='red')

plt.title('Actual vs Forecasted Values')
plt.xlabel('Time')
plt.ylabel('Order Size')
plt.legend()
plt.grid(True)
plt.savefig('ForecastVsActual.png')
plt.show()

