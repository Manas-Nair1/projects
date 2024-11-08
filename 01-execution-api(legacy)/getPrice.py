
import requests
import time

# KuCoin Futures API endpoint
BASE_URL = "https://api-futures.kucoin.com/api/v1"

def get_last_price(symbol):
    """
    Fetches the last price for a given futures contract from KuCoin Futures API.
    
    :param symbol: The futures contract symbol (e.g., "XBTUSDTM").
    :return: The last traded price.
    """
    endpoint = f"/ticker?symbol={symbol}"
    url = BASE_URL + endpoint

    try:
        response = requests.get(url)
        data = response.json()

        if data['code'] == "200000":
            last_price = data['data']['price']
            return last_price
        else:
            print(f"Error fetching price: {data['msg']}")
            return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

if __name__ == "__main__":
    symbol = "ETHUSDTM"  # Replace with your desired futures contract symbol
    while True:
        price = get_last_price(symbol)
        if price:
            print(f"Last price for {symbol}: {price}")
        time.sleep(5)  # Fetch price every 5 seconds (adjust as needed)
