import numpy as np
import ccxt
import scipy.stats as stats
import time



exchange = ccxt.kucoinfutures({
    'rateLimit': 2000,
    'enableRateLimit': True,
    'adjustForTimeDifference': True,
    "apiKey": '',
    "secret": '',
    "password": '',
})
symbol = 'ETH/USDT:USDT'
start_time = time.time()
ticker = exchange.fetch_ticker(symbol)

def ask_bid(symbol=symbol):
    ob = exchange.fetch_order_book(symbol)
    bid = ob['bids'][0]
    ask = ob['asks'][0]
    # print(f'this is the ask of {symbol} {ask}')
    # print(f'this is the bid for {symbol} {bid}')
    return ask, bid

def df_trades_to_numpy(symbol=symbol):
    trades = exchange.fetch_trades(symbol)

    trade_amounts = []
    min_trade_size = 0.1

    for trade in trades:
        trade_size = trade['amount']
        if trade_size >= min_trade_size:
            # Adjust the amount based on the 'side' (sell or buy)
            if trade['side'] == 'sell':
                trade_amount = -trade_size
            elif trade['side'] == 'buy':
                trade_amount = trade_size
            trade_amounts.append(trade_amount)

    trade_amount_array = np.array(trade_amounts)

    return trade_amount_array

array = df_trades_to_numpy()
print(array)
mean_amount = np.mean(array)
std_dev_amount = np.std(array)

def probability_up():
    """
    should calculate probability based on a tuple of information: (price, amount)
    so it takes the info about amt and uses the norm distribution to evaluate the prob of an order moving price to that level
    """
    orderbook = ask_bid() 
    ask_price = orderbook[0][0]
    amount_to_move = -(orderbook[0][1])
    #probability will be P(X < amount to move)
    probability = stats.norm.cdf(amount_to_move, loc=mean_amount, scale=std_dev_amount)
    # print(amount_to_move)
    return ask_price, round(probability,2)
    


def probability_down():
    orderbook = ask_bid() 
    bid_price = orderbook[1][0]
    amount_to_move = (orderbook[1][1])
    #probability will be P(X > amount_to_move) 
    probability = 1 - stats.norm.cdf(amount_to_move, loc=mean_amount, scale=std_dev_amount)
    # print(amount_to_move)
    return bid_price, round(probability,2)


x = probability_up()
y = probability_down()
end_time = time.time()
print(x,y)
print(end_time-start_time)