import requests

import pandas as pd 
import time

# Step 1: Define the function to fetch Kline data
def _fetch_kline_data(symbol='XBTUSDTM',granularity=1,):
    url = f'https://api-futures.kucoin.com//api/v1/kline/query?symbol={symbol}&granularity={granularity}'
    response = requests.get(url)
    response_data = response.json()
    
    if response_data['code'] != '200000':
        raise Exception(f"Error fetching Kline data: {response_data}")
    return response_data['data']

# Step 2: Fetch Kline data and print the results
def getKline(symbol,granularity=1):
    try:
        kline_data = _fetch_kline_data(symbol=symbol,granularity=granularity)
        df = (pd.DataFrame(kline_data))
        df[0] = pd.to_datetime(df[0], unit='ms')
        df.rename(columns={
            0: 'Timestamp',
            1: 'Open',
            2: 'High',
            3: 'Low',
            4: 'Close',
            5: 'Volume'
        }, inplace=True)

        return df
    
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    df = (getKline('ETHUSDTM',granularity=1))
    print(df)