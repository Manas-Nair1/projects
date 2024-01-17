# Backtesting strategies
First we backtest the mean-reverting pairs strategy discussed at [CaseStudy:BTCvsETH](Modeling OU processes/CaseStudy:BTCvsETH). We will use a relatively simple strategy where if the z-score of the ratios at any given moment are far enough away from the mean(relative to a given threshold), we take opposite positions in the 2 assets until the asset price ratios revert to their long-run mean.
Guide: https://www.youtube.com/watch?v=f73ItMWO4z8

# Signal_generator.py
We will first work on generating signals using the ratios.csv file. The signal generator will look for the ratio to be outside some predetermined limit and will put buy or sell orders into another csv file. Backtest.py will use the timestamp and then buy/sell depending on the signal. It will then ohlcv data and close positions when the ratio returns to the long-run mean. Ohlcv data allows us to extrapolate the P/L for each trade governed by the signal.
Ratio is (ETH/BTC) meaning if z-score is negative, BTC is over-performing and ETH is underperforming, thus we should short BTC and long ETH.

# Backtest.py
takes the signals generated and applies a simple backtest. It will take the signal, "long" for instance, and take the respective positions (long in ETH and short in BTC). It will then wait for the z-score to return to a range close to 0 
(|z| < 0.3). Results are available under Jupyter Notebook. 