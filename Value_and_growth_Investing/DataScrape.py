"""
Fetches and calculates EV/EBITDA to compare against a threshold which is found from the 'industry average.'
"""
import pandas as pd

def extract_symbols_from_file(file_path):
    symbols = []
    with open(file_path, 'r') as file:
        # Skip the header line assuming it contains the titles
        next(file)
        
        # Process each line in the file
        for line in file:
            # Split the line by '|' character
            data = line.strip().split('|')
            
            # Extract the symbol (assuming it's the first element)
            symbol = data[0]
            
            # Append the symbol to the list
            symbols.append(symbol)
    
    return symbols

# Replace 'file_path.txt' with the path to your actual file
file_path = 'Value_and_growth_Investing/nasdaqlisted.txt'  # Change this to your file path
extracted_symbols = extract_symbols_from_file(file_path)

# Print the extracted symbols
print("Extracted Symbols:")
print(extracted_symbols)
print(len(extracted_symbols))

import yfinance as yf

def get_industry(stock_ticker):
    # Get stock information
    stock = yf.Ticker(stock_ticker)
    
    # Retrieve sector or industry information from the stock data
    industry = stock.info.get('sector', 'Industry information not found')
    
    return industry

def get_ev_ebitda_ratio(stock_ticker):
    try:
        # Get stock information
        stock = yf.Ticker(stock_ticker)
        
        # Get financial data
        financials = stock.info
        
        # Extract EV and EBITDA if available
        if 'enterpriseValue' in financials and 'ebitda' in financials:
            ev = financials['enterpriseValue']
            ebitda = financials['ebitda']
            
            # Calculate EV/EBITDA ratio
            ev_ebitda_ratio = ev / ebitda
            
            return ev_ebitda_ratio
        else:
            return "Information not available"

    except Exception as e:
        return f"Error fetching data for {stock_ticker}: {e}"

ticker_ratios = []
for ticker in extracted_symbols:
    try:
        print("\n" + ticker)
        industry = get_industry(ticker)
        print(industry)
        ratio = get_ev_ebitda_ratio(ticker)
        print(ratio)
        ticker_ratios.append([ticker,industry, ratio])
    except:
        pass
df = pd.DataFrame(ticker_ratios, columns=['Ticker', 'Industry', 'Ratio'])
df.to_csv('NasdaqRatios.csv')
print(df)