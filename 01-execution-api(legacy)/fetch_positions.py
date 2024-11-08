
from kucoin.base_request.base_request import KucoinBaseRestApi
import json

# Your API key details
api_key = ''
api_secret = ''
api_passphrase = ''

class KucoinPositionsAPI(KucoinBaseRestApi):
    def get_positions(self):
        """
        Fetch open positions from KuCoin API.
        """
        # Define the endpoint for positions
        uri = '/api/v1/positions'
        
        # Make the GET request using the inherited _request method
        response = self._request('GET', uri, timeout=5, auth=True)
        
        return response

# Initialize the Kucoin API with your credentials
def fetchPositions(symbol=None):
    api = KucoinPositionsAPI(key=api_key, secret=api_secret, passphrase=api_passphrase, url='https://api-futures.kucoin.com')
    try:
        if "code" in api.get_positions():
            return []
        if symbol is not None:
            for position in api.get_positions():
                if position.get("symbol") == symbol:
                    return position  # Return the matching dict
        # print(api.get_positions())
        return api.get_positions()
    except KeyError as e:
        return []

if __name__ == "__main__":

    positions = fetchPositions("ETHUSDTM")
    print(positions)

