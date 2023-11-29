The objective of this study is to conduct a comprehensive time series analysis of historical executed trades on the exchange. The primary hypothesis is that discernible patterns exist within the trade execution data, indicating potential opportunities for predictive modeling and strategic decision-making. Leveraging statistical techniques including Augmented Dickey-Fuller (ADF) tests, visual analysis of trends and seasonality, and the examination of rolling statistics, this study aims to ascertain the stationarity of the trade data and identify any underlying patterns or dependencies. Additionally, the research will explore the potential impact of outliers, perform residual diagnostics on models, and consider transformation techniques to enhance the stationarity of the time series data. The ultimate goal is to derive actionable insights that could facilitate more informed trade execution strategies and risk management in the exchange market

#Data collection and preparation
This part is reasonably straightforward. The API calls necessary have already been used in the TradingEngine/testAPI.py file. Trades executed and orderbook data will be saved into 2 separate CSV files. Aim is to use ADF and KPSS tests to test for unit roots and stationarity and use the Hurst exponent to test for mean reversion, and will format data to work with the respective libraries used for the stastical tests. 

#Applying tests and evaluating results
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

These tests were run with a small dataset that was collected over the length of 1h. More data should help make more definite conclusions. These results suggest that the time series may be stationary. 
# arma model
ARMA.py aims to build a predictive model. The results are plotted under ForcastVsActual.png. The main problem that arises is the high variance of the dataset. Although it may show stationary behaviour, the high variance leads to any single predicted value being wrong with a high likelyhood. A better application maybe to calculate the summary statistics for the given dataset and then try and use that to build a probility density function. 