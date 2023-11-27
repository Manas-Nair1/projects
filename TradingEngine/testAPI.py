"""

Goal is to test API calls and test how long they take. 
Will calculate various indicators to experiment with API responses but these have nothing to do
with the actual strategy
the strategy was heavily inspired by article at:
https://www.quantifiedstrategies.com/relative-strength-index-and-moving-average-trading-strategy/

"""

import ccxt
import pandas as pd
import numpy as np
import time
from datetime import datetime


exchange = ccxt.kucoinfutures({
    #key and secret must be added before connection to exchange can be established
    'rateLimit': 2000,
    'enableRateLimit': True,
    'adjustForTimeDifference': True,
    "apiKey": '',
    "secret": '',
    "password": '',
})

def fetch_ohlcv_data(symbol, timeframe, limit=100):
    ohlcv = exchange.fetch_ohlcv(symbol, timeframe, limit=limit)
    df = pd.DataFrame(ohlcv, columns=['timestamp', 'open', 'high', 'low', 'close', 'volume'])
    df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms')
    df.set_index('timestamp', inplace=True)
    return df

def calculate_obv_past_day(df):
    df['obv'] = 0
    df['obv'] = df['volume'].diff().fillna(0).cumsum()
    
   
    df['obv'] = df['obv'] - df['obv'].shift(1)
    
    return df


def calculate_rsi(df, window=14):
    delta = df['close'].diff(1)
    gain = delta.where(delta > 0, 0)
    loss = -delta.where(delta < 0, 0)

    avg_gain = gain.rolling(window=window, min_periods=1).mean()
    avg_loss = loss.rolling(window=window, min_periods=1).mean()

    rs = avg_gain / avg_loss
    rsi = 100 - (100 / (1 + rs))

    df['rsi'] = rsi
    return df


def calculate_sma(df, window=20):
    df['sma'] = df['close'].rolling(window=window).mean()
    return df

symbol = 'BTC/USDT:USDT'


def ask_bid(symbol=symbol):
    ob = exchange.fetch_order_book(symbol)
    bid = ob['bids'][0][0]
    ask = ob['asks'][0][0]
    # print(f'this is the ask of {symbol} {ask}')
    # print(f'this is the bid for {symbol} {bid}')
    return ask, bid

def go_long(rsi, sma, obv):
    if rsi <= 35 and obv >= 0:
        return True
    else: 
        return False

def go_short(rsi, sma, obv):
    if rsi >= 70 and obv <= 0:
        return True
    else:
        return False
    

# works with majority of timeframes available on Tradingview

timeframe = '5m'

#-----------------------------------------------------------
# trade execution here on


sma_window = 20
run = True
st_loss = 0.999 #identify stop loss 
tk_prof = 1.003 #identify take profit 
short_loss = 1.001
short_profit = 0.997
buy_price = 0 #initialize buy price
sell_price = 0 #for short
size = 1
side = None
current_postion = 0 


def execute_long():
    print(f"Conditions met. Going long at {current_price}")
    print(f'stop loss will be at {current_price*st_loss}')
    print(f'take profit will be at {current_price*tk_prof}')
    buy_price = current_price
    exchange.create_limit_buy_order(symbol, size, buy_price, {'leverage': 30})
    exchange.create_limit_sell_order(symbol, size, current_price*0.999,{'stopLossPrice':current_price*0.999, 'reduceOnly': True})
    exchange.create_limit_sell_order(symbol, size, current_price*1.003,{'takeProfitPrice':current_price*1.003, 'reduceOnly': True})
    return

def execute_short():
    print(f"Conditions met. Going short at {current_price}")
    print(f'stop loss will be at {current_price*short_loss}')
    print(f'take profit will be at {current_price*short_profit}')
    sell_price = current_price
    exchange.create_limit_sell_order(symbol, size, current_price, {'leverage': 30})
    exchange.create_limit_buy_order(symbol, size, current_price*1.001, {'stopLossPrice':current_price*1.001, 'reduceOnly': True})
    exchange.create_limit_buy_order(symbol, size, current_price*0.997, {'takeProfitPrice':current_price*0.997, 'reduceOnly': True})
    return

#-----------------------------------------------------------


while run == True:
    now = datetime.now()
    position = 0

    ohlcv_data = fetch_ohlcv_data(symbol, timeframe)
    
    ohlcv_data = calculate_obv_past_day(ohlcv_data)
    
    ohlcv_data = calculate_rsi(ohlcv_data)
    
    ohlcv_data = calculate_sma(ohlcv_data, window=sma_window)
    
    obv_value = ohlcv_data.iloc[-1]['obv']
    rsi_value = ohlcv_data.iloc[-1]['rsi']
    sma_value = ohlcv_data.iloc[-1]['sma']
    current_price = ask_bid(symbol)[0] 

    print('\n',now)
    
    if go_long(rsi_value, sma_value, obv_value) == True:
        execute_long()

    if go_short(rsi_value, sma_value, obv_value) == True:
        execute_short()
    else:
        print('Conditions not met')
        print(f'\nOBV value for the past {timeframe}: {obv_value}')
        print(f'RSI value for the past {timeframe}: {rsi_value}')
        print(f'SMA value for the past {timeframe}: {sma_value}')
        print(f'the current price is {current_price}')
    
    time.sleep(30)  


 
