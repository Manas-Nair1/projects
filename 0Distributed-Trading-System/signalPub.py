'''
This uses a transformer based model to label entries. IP's are on a VPN and not open to the public. 
'''

import torch
import pandas as pd
import numpy as np
import joblib
import time
import logging
import zmq  # Importing ZeroMQ library for Pub/Sub
from torch.utils.data import DataLoader, TensorDataset
from nanoGPTforecast import GPT, GPTConfig
from CVCpy_link.Backtesting.newExpert import ExpertAdvisor
from CVCpy_link.utils.datasetObject import datasetObject
from wsku.ohlcv import getKline
from wsku.getPrice import get_last_price
from wsku.allUtils import broker
from datetime import datetime
from runPred import GPTPrediction
from wsku.exec import fetchPositions

# Initialize the broker instance
myBroker = broker()

# Store active positions with their entry prices
active_positions = {"long": None, "short": None}

# Set up logging
logging.basicConfig(filename='A:\\trade_logs.log', level=logging.INFO, 
                    format='%(asctime)s - %(levelname)s - %(message)s')

# Initialize ZeroMQ context and publisher socket
context = zmq.Context()
socket = context.socket(zmq.PUB)
socket.bind("tcp://100.98.252.86:5555")

def close_position(position_type, symbol):
    """Close the position and reset the active position tracking."""
    if position_type == "long" and active_positions["long"] is not None:
        myBroker.close_positions(symbol)
        active_positions["long"] = None
        logging.info(f"Closed long position on {symbol}")

    if position_type == "short" and active_positions["short"] is not None:
        myBroker.close_positions(symbol)
        active_positions["short"] = None
        logging.info(f"Closed short position on {symbol}")

def publish_to_zeromq(channel, message):
    """Publish data to ZeroMQ."""
    socket.send_string(f"{channel} {message}")

def main():
    global active_positions  # Declare active_positions as global

    symbol = "ETHUSDTM"
    
    # Reset active_positions if no open positions are found
    if fetchPositions(symbol) == []:
        active_positions = {"long": None, "short": None}
    
    # Fetch historical data
    df_5m = getKline(symbol, granularity=5)
    df_15m = getKline(symbol, granularity=15)
    df_30m = getKline(symbol, granularity=30)
    df_1h = getKline(symbol, granularity=60)

    # Process the data with ExpertAdvisor
    processor = datasetObject.from_dataframes(df_5m, df_15m, df_30m, df_1h)
    ea = ExpertAdvisor(processor)
    ea.computeMomentum()
    ea.computeDirectional()
    ea.computeCore()
    df = ea.backtesting

    # Run GPT predictions
    preds = GPTPrediction.run_prediction(
        df=df,
        model_path='A:\\ETHm30_gpt_model.pth',
        scaler_path='A:\\ETHm30gptScaler.pkl',
        output_path=''
    )
    print(preds.tail(5))

    # Get the last prediction label
    LastLabel = preds.iloc[-1]['Predicted_Label']
    
    # Log the LastLabel value
    logging.info(f"LastLabel for {symbol}: {LastLabel}")
    
    last_price = float(get_last_price(symbol))

    # Collect OHLCV data (Open, High, Low, Close, Volume)
    ohlcv_data = {
        'timestamp': datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S'),
        'last_label': LastLabel,
        'ohlcv': {
            'Open': df_5m['Open'].iloc[-1],
            'High': df_5m['High'].iloc[-1],
            'Low': df_5m['Low'].iloc[-1],
            'Close': df_5m['Close'].iloc[-1],
            'Volume': df_5m['Volume'].iloc[-1],
        },
        'last_price': last_price
    }

    # Publish the OHLCV data to ZeroMQ
    publish_to_zeromq('market_data', str(ohlcv_data))

# Continuously monitor the market and trade
while True:
    main()
    time.sleep(60*5)