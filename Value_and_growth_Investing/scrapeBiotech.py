import pandas as pd 
import numpy as np
import yfinance as yf

import matplotlib.pyplot as plt





try:
    stocksdf = pd.read_csv("Value_and_growth_Investing/biotechTemp.csv")
    print(stocksdf.tail())
except:
    

    df = pd.read_csv("Value_and_growth_Investing/NasdaqRatios.csv")

    print(df.tail())

    healthcare_stocks = []
    for index, value in df.iterrows():
        if value.Industry == "Healthcare":
            healthcare_stocks.append(value.Ticker)
            
    # print(len(healthcare_stocks))

    stocks_income = []
    for ticker in healthcare_stocks:
        try:
            stock = yf.Ticker(ticker)
            # print(stock.info['enterpriseValue'])
            net_income = stock.info['enterpriseValue'] #financials.loc['Total Revenue']
            # print(net_income)
            stocks_income.append([ticker,net_income])
        except:
            pass
    # print(stocks_income[-1])

    stocksdf = pd.DataFrame(stocks_income, columns=['ticker','income'])
    print(stocksdf.tail())
    stocksdf.to_csv('biotechTemp.csv')


income_lst = stocksdf['income'].tolist()

plt.figure(figsize=(8, 6))
plt.hist(stocksdf['income'], bins=10, edgecolor='black')  # Adjust the number of bins as needed
plt.xlabel('Income')
plt.ylabel('Number of Data Points')
plt.title('Distribution of Income')
plt.grid(True)
plt.savefig("incomecluster.png")
plt.show()

# mean = np.mean(income_lst)
# stdev = np.std(income_lst)
# print(mean, stdev)

# first_quartile = np.percentile(income_lst, 25)

# third_quartile = np.percentile(income_lst, 87.5)

# print("First Quartile (Q1):", first_quartile)
# print("Third Quartile (Q3):", third_quartile)
