
from kucoin.base_request.base_request import KucoinBaseRestApi
import uuid  # for generating unique clientOid
import logging

# Your API key details
api_key = ''
api_secret = ''
api_passphrase = ''

# Define Kucoin Order API class
class KucoinOrderAPI(KucoinBaseRestApi):
    def create_order(self, order_params):
        """
        Place an order using the parameters provided by the user.
        :param order_params: Dictionary of parameters required for the order.
        """
        uri = '/api/v1/orders'
        # Make the POST request using the provided parameters
        response = self._request('POST', uri, params=order_params, timeout=5, auth=True)
        return response

# Initialize API instance
api = KucoinOrderAPI(key=api_key, secret=api_secret, passphrase=api_passphrase, url='https://api-futures.kucoin.com')

def place_order(symbol, side, price, leverage=30,size=1, stop=None, stop_price_type=None, stop_price=None, reduce_only=False, timeInForce = None):
    """
    Place an order on KuCoin, with optional stop parameters for stop orders.
    :param symbol: Trading symbol (e.g., "XBTUSDTM")
    :param side: Order side (buy or sell)
    :param price: Limit price
    :param leverage: Leverage for the order
    :param stop: Type of stop (up or down)
    :param stop_price_type: Stop price type (TP, IP, MP)
    :param stop_price: Stop price value
    :param reduce_only: Set to True for reduce-only orders (e.g., Stop Loss or Take Profit)
    """
    
    # Basic order parameters
    order_params = {
        "clientOid": str(uuid.uuid4()),  # Unique order ID
        "side": side,                    # Buy or Sell
        "symbol": symbol,                # Example symbol
        "leverage": leverage,            # Leverage, e.g., 30x
        "type": "limit",                 # Order type (limit or market)
        "price": price,                  # Limit price (for market, set it to None)
        "size": size,                       # Order size (required)
        "reduceOnly": reduce_only,
        # 'postOnly' : True
    }
    # if timeInForce:
    #     order_params.update({
    #         'timeInForce' : timeInForce
    #     })
    # Add stop order parameters if provided
    if stop and stop_price_type and stop_price:
        order_params.update({
            "stop": stop,                      # 'up' or 'down'
            "stopPriceType": stop_price_type,   # TP, IP, or MP
            "stopPrice": stop_price             # Stop price
        })
    
    try:
        # Call the create_order method and pass the order parameters
        response = api.create_order(order_params)
        logging.debug(f"Order Response: {response}")
        print(f"Order placed successfully: {response}")
    except Exception as e:
        logging.error(f"Error placing order: {e}")
        print(f"Failed to place order: {e}")

if __name__ == "__main__":
    symbol = "XBTUSDTM"
    buy_price = "60000"  # Price to open the position with a limit buy order
    leverage = 30
    
    # Place main limit buy order to open a position
    print("Placing limit buy order...")
    place_order(symbol, "buy", buy_price, leverage)
    
    # Let's assume the current price is 60,000 (in practice, you'd fetch this dynamically)
    current_price = 60000
    
    # Calculate 3% above and below for stop orders
    stop_loss_price = round(current_price * 0.97, 2)  # 3% below the current price
    take_profit_price = round(current_price * 1.03, 2)  # 3% above the current price

    # Place Stop Loss reduce-only order
    print("Placing stop-loss order...")
    place_order(
        symbol, 
        "sell", 
        price=str(stop_loss_price),  # No limit price for stop orders
        leverage=leverage, 
        stop="down",  # Stop Loss type
        stop_price_type="MP",  # Market price (MP)
        stop_price=str(stop_loss_price), 
        reduce_only=True  # This is a reduce-only order
    )
    
    # Place Take Profit reduce-only order
    print("Placing take-profit order...")
    place_order(
        symbol, 
        "sell", 
        price=str(take_profit_price),  # No limit price for stop orders
        leverage=leverage, 
        stop="up",  # Take Profit type
        stop_price_type="MP",  # Market price (MP)
        stop_price=str(take_profit_price), 
        reduce_only=True  # This is a reduce-only order
    )
