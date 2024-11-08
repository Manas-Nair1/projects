from placeOrder import place_order
from exec import fetchPositions
import time

class broker:
    def __init__(self) -> None:
        pass

    def execute_long(self, symbol, price, size=1, leverage=50, tp=0.008, sl=0.003):
        try:  
            print("Placing main long order...")
            place_order(
                symbol, 
                "buy", 
                price=str(round(price*1.0005,1)),  
                leverage=str(leverage), 
                size=size,
            )

            stop_loss_price = round(price - price*sl, 1)
            stop_loss_trigger = round(price - price*(sl - 0.001), 1)  # Trigger slightly earlier than SL

            take_profit_price = round(price + price*tp, 1)
            take_profit_trigger = round(price + price*(tp - 0.001), 1)  # Trigger slightly earlier than TP

            print(f"Stop Loss: {stop_loss_price} (trigger: {stop_loss_trigger}), Take Profit: {take_profit_price} (trigger: {take_profit_trigger})")

            # Place Stop Loss reduce-only order
            print("Placing stop-loss order...")
            place_order(
                symbol, 
                "sell", 
                price=str(stop_loss_price),
                leverage=str(leverage), 
                stop="down",  
                stop_price_type="MP",  
                stop_price=str(stop_loss_trigger),  # Trigger earlier to prevent slippage
                reduce_only=True
            )
            
            # Place Take Profit reduce-only order
            print("Placing take-profit order...")
            place_order(
                symbol, 
                "sell", 
                price=str(take_profit_price),
                leverage=str(leverage), 
                stop="up",  
                stop_price_type="MP",  
                stop_price=str(take_profit_trigger),  # Trigger earlier to prevent slippage
                reduce_only=True
            )

        except Exception as e:
            return f'{e}'

    def execute_short(self, symbol, price, size=1, leverage=50, tp=0.008, sl=0.003):
        try:  
            print("Placing main short order...")
            place_order(
                symbol, 
                "sell", 
                price=str(round(price*0.9995,1)),  
                leverage=str(leverage), 
                size=size,
            )

            stop_loss_price = round(price + price*sl, 1)
            stop_loss_trigger = round(price + price*(sl - 0.001), 1)  # Trigger earlier than SL

            take_profit_price = round(price - price*tp, 1)
            take_profit_trigger = round(price - price*(tp - 0.001), 1)  # Trigger earlier than TP

            print(f"Stop Loss: {stop_loss_price} (trigger: {stop_loss_trigger}), Take Profit: {take_profit_price} (trigger: {take_profit_trigger})")

            # Place Stop Loss reduce-only order
            print("Placing stop-loss order...")
            place_order(
                symbol, 
                "buy", 
                price=str(stop_loss_price),
                leverage=str(leverage), 
                stop="up",  
                stop_price_type="MP",  
                stop_price=str(stop_loss_trigger),  # Trigger earlier to prevent slippage
                reduce_only=True,
                size=size
            )
            
            # Place Take Profit reduce-only order
            print("Placing take-profit order...")
            place_order(
                symbol, 
                "buy", 
                price=str(take_profit_price),
                leverage=str(leverage), 
                stop="down",  
                stop_price_type="MP",  
                stop_price=str(take_profit_trigger),  # Trigger earlier to prevent slippage
                reduce_only=True,
                size=size
            )

        except Exception as e:
            print("Error occurred")
            print(e)
            return f'{e}'


    def close_positions(self,symbol):
        try:
            positon = fetchPositions(symbol=symbol)
            print(positon)
            price = round(positon['markPrice'],1)
            if positon['currentQty'] < 0:
                #close short
                place_order(
                    symbol, 
                    "buy", 
                    price=str(price), 
                    size=str(-1*positon['currentQty']),
                    reduce_only=True
                )
            if positon['currentQty'] > 0:
                #close long
                place_order(
                    symbol, 
                    "sell", 
                    price=str(price),
                    size=str(positon['currentQty']),
                    reduce_only= True
                )
            time.sleep(10)
            positon = fetchPositions(symbol=symbol)
            if len(positon) !=0:
                return self.close_positions(symbol)
        except Exception as e:
            print(e)
        return
if __name__ == "__main__":
    myBroker = broker()
    # Example of calling execute_short with custom TP/SL values
    print(myBroker.close_positions("XBTUSDTM"))