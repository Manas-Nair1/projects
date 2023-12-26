'''
Should compare the ratios in ratios.csv file to the industryAverage.csv file for that industry 
and return any tickers that have z scores outside a threshold
current threshold is set to 2 stdevs away from mean
'''
import pandas as pd
from summary_stats import new_df, averages_df

print(new_df.tail(),"\n" ,averages_df)

# print(averages_df.loc[averages_df['Industry'] == 'Healthcare', 'Mean'].values[0])
stocks_to_watch = []
for index, value in new_df.iterrows():
    ticker = value.Ticker
    industry = value.Industry
    ratio = value.Ratio
    mean = averages_df.loc[averages_df['Industry'] == industry, 'Mean'].values[0]
    stdev = averages_df.loc[averages_df['Industry'] == industry, 'Stdev'].values[0]
    z_score = (float(ratio) - float(mean))/float(stdev)
    if abs(z_score) > 1.5:
        print(z_score, ticker)
        stocks_to_watch.append(ticker)
        
stocksdf = pd.DataFrame(stocks_to_watch, columns=['ticker'])
print(stocksdf)
stocksdf.to_csv('stocks.csv')