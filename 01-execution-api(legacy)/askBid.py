import asyncio
import json
import requests
from datetime import datetime
import websockets

# Step 1: Get the Public Token
def get_ws_info():
    url = 'https://api.kucoin.com/api/v1/bullet-public'
    response = requests.post(url)
    response_data = response.json()
    
    if response_data['code'] != '200000':
        raise Exception(f"Error fetching WebSocket info: {response_data}")
    
    return response_data

# Step 2: Connect to the WebSocket
async def connect_to_ws(ws_url, token):
    ws_url_with_token = f"{ws_url}?token={token}"
    
    while True:
        try:
            async with websockets.connect(ws_url_with_token) as ws:
                print("Connected to WebSocket")
                
                # Step 3: Get All Supported Trading Pairs
                symbols_response = requests.get('https://api.kucoin.com/api/v1/symbols')
                symbols_data = symbols_response.json()
                if symbols_data['code'] != '200000':
                    raise Exception(f"Error fetching symbols: {symbols_data}")
                
                # Print all supported trading pairs
                # print("Supported Trading Pairs:")
                # for symbol in symbols_data['data']:
                #     print(symbol['symbol'])
                
                # Step 4: Subscribe to Trading Data
                subscribe_message = {
                    "type": "subscribe",
                    "topic": "/contractMarket/level2Depth50:XBTUSDTM",  # Example topic
                    # "topic": "/contractMarket/execution:XBTUSDTM",
                    "response": True
                }
                await ws.send(json.dumps(subscribe_message))
                
                # Handle responses
                while True:
                    response = await ws.recv()
                    data = json.loads(response)
                    # Print the entire response with the converted timestamp
                      # Add a human-readable timestamp to the data
                    data['timestamp'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                    
                    print("Received Data:")
                    print(json.dumps(data, indent=4))  # Pretty-print the response
                    
                    with open('A:\\askbidLVL2XBTC9-17.log', 'a') as file:
                        file.write(json.dumps(data) + '\n')

        except websockets.ConnectionClosedError as e:
            print(f"Connection closed with error: {e}. Reconnecting...")
            await asyncio.sleep(5)  # Wait before trying to reconnect

        except Exception as e:
            print(f"Unexpected error: {e}. Reconnecting...")
            await asyncio.sleep(5)  # Wait before trying to reconnect

async def main():
    # Get WebSocket URL and Token
    ws_info = get_ws_info()
    ws_url = ws_info['data']['instanceServers'][0]['endpoint']
    token = ws_info['data']['token']

    # Connect and Subscribe
    await connect_to_ws(ws_url, token)

if __name__ == "__main__":
    asyncio.run(main())
