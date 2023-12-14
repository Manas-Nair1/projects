## WIP
# Summary
This project aims to create algorithms that use principles of value investing to find "under-valued" or "over-valued" companies. It does this by querying the EV/EBITDA ratio for a given company against a industry average as sourced by the NYU dataset[1].
A secondary goal is to find/generate datasets for EV/EBITDA ratios as a timeseries and identify timeframes of extraordinarily high or low values. News, press releases, and coporate changes should then be queried from this timeframe. A deep learning model could then be trained to identify what causes large changes to EV/EBITDA in that specific sector. 
More of a pure datascience project
# DataScrape.py
uses a list of all stocks on the nasdaq and uses yfinance to find its sector, enterprise value, and Earnings Before Interest, Taxes, Depreciation, and Amortization
# Summary stats.py
Generates industry means and standard deviations for tickers from dataScrape.py
# Screener.py
returns stocks with ratios that are some given threshold away from their mean. 


[1] https://pages.stern.nyu.edu/~adamodar/New_Home_Page/datafile/vebitda.html