The objective of this study is to conduct a comprehensive time series analysis of historical executed trades on the exchange and cross reference them with the limit orders present on the orderbook. The primary hypothesis is that discernible patterns exist within the trade execution data, indicating potential opportunities for predictive modeling. Leveraging statistical techniques including Augmented Dickey-Fuller (ADF) tests, visual analysis of trends and seasonality, and the examination of rolling statistics, this study aims to ascertain the stationarity of the trade data and identify any underlying patterns or dependencies. 

# Data collection and preparation
This part is reasonably straightforward. The API calls necessary have already been used in the TradingEngine/testAPI.py file. Trades executed and orderbook data will be saved into 2 separate CSV files. Aim is to use ADF and KPSS tests to test for unit roots and stationarity and use the Hurst exponent to test for mean reversion, and will format data to work with the respective libraries used for the stastical tests. 

# Applying tests and evaluating results
ADF Statistic: -7.079215189338646
p-value: 4.714044034087991e-10
Critical Values:
        1%: -3.4578942529658563
        5%: -2.8736593200231484
        10%: -2.573228767361111
KPSS Statistic: 0.15651817593214315
p-value: 0.1
Critical Values:
   10%: 0.347
   5%: 0.463
   2.5%: 0.574
   1%: 0.739

These tests were run over a relatively small dataset. More data should help make more definite conclusions. These results suggest that the time series may be stationary. 
# arma model
ARMA.py builds a predictive model. The results are plotted under ForcastVsActual.png. The main problem is due to the high variance of the dataset. Although it may show stationary behaviour, the high variance makes it very difficult to predict an exact value for the Trades(n+1). A better application maybe to calculate the summary statistics for the given dataset and then try and use that to build a probility density function that can use the range of possible values to build a model. 

# Trades vs Orderbook
This script aims to use the fact that the r.v. denoting trades executed for the n'th time period (T<sub>n</sub>) displays stationary behaviour. It generates a normal distribution model to predict probability of the next value of T<sub>n+1</sub> being greater or smaller than the amount needed to affect the orderbook substantially. It looks at the state of the orderbook, stores the values of the highest bid and lowest ask and calculates the probability of the next value of T<sub>n</sub> being large enough in either direction to engulf either of these limit orders. The orderbook's limit orders could also be modeled as its own r.v. For the sake of this model, **I assume no hidden orders, order spoofing, or skewed distributions of this r.v.** It is most likely not entirely stochastic and could be modeled on its own.

# Improvements
Time needed for exectuion needs to be improved. It takes ~25 seconds per calculation and the HFT nature of the strategy makes this way too long to ever be profitable. Majority of the slowdown is due to the API calls
The data used to generate the PDF for the T<sub>n</sub> should not just be the most recent 20 trades, but a bigger sample over a longer time period. 
The strategy should be backtested in local environment. 