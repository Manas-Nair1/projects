"""
Should be able to gather data over timeframe in question and plot figures which help us determine if a relationship exists
source: Successful algorithmic trading by Michael Halls-Moore
"""
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

def get_stock_data(stocks, start_date, end_date):
    data = {}
    for stock in stocks:
        data[stock] = yf.download(stock, start=start_date, end=end_date)['Close']
    return pd.DataFrame(data)

# Define the stocks and time range
stocks = ['MRK', 'BMY']  # Example stocks (Apple and Microsoft)
start_date = '2017-01-01'  # Start date
end_date = '2018-01-01'    # End date

# Get the stock data
stock_data = get_stock_data(stocks, start_date, end_date)
print(stock_data.tail())  # Display the first few rows of the DataFrame

def plot_price_series(price_df):
    """
    Plot the Adjusted Close price series for XOM and USO.

    Parameters
    ----------
    price_df : `pd.DataFrame`
        A DataFrame containing XOM and USO Adjusted Close data from
        01/01/2019-01/01/2020. Index is a Datetime object.

    Returns
    -------
    None
    """
    fig = price_df.plot(title="ABBV and RHHBY Daily Prices")
    fig.set_ylabel("Price($)")
    plt.savefig('visualAnalysis.png')
    plt.show()

plot_price_series(stock_data)
def plot_scatter_series(price_df):
    """
    Plot the Scatter plot of the XOM and USO price series.

    Parameters
    ----------
    price_df : `pd.DataFrame`
        A DataFrame containing XOM and USO Adjusted Close data from
        01/01/2019-01/01/2020. Index is a Datetime object.
    
    Returns
    -------
    None
    """
    price_df.plot.scatter(x=0, y=1, title="ABBV and RHHBY Price Scatterplot")
    plt.savefig('scatter.png')
    plt.show()

plot_scatter_series(stock_data)

# Assuming your DataFrame is named 'df'
# for index, row in stock_data.iterrows():
#     if row['RHHBY'] < 35 and row['ABBV'] > 85:
#         print(f"Date: {index} - ABBV: {row['ABBV']}, RHHBY: {row['RHHBY']}")
