'''
IP's are on a VPN and not open to the public. 
'''
import zmq

context = zmq.Context()
socket = context.socket(zmq.SUB)
socket.connect("tcp://100.98.252.86:5555")
socket.subscribe(b"market_data")  # Subscribe to the 'market_data' channel

while True:
    message = socket.recv_string()  # Receive the message
    print(f"Received: {message}")