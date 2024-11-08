Distributed Trading System with ZeroMQ

This project demonstrates the development of a distributed trading system using ZeroMQ to manage real-time market data and orchestrate multiple worker components for live trading. The system features a server that runs trading algorithms on live market data, communicates using the pub/sub messaging pattern via ZeroMQ, and coordinates multiple worker processes that handle different tasks such as entering and exiting positions.

Overview

The trading system architecture consists of:

	•	Server: This component fetches live market data, processes trading signals, and publishes them to the workers via a ZeroMQ publish socket. It also runs the core trading algorithms that generate buy/sell signals based on real-time data.
	•	Workers: Each worker subscribes to the signals broadcast by the server and performs specific tasks:
	•	Position Entering Worker: This worker listens for buy/sell signals from the server and enters positions accordingly.
	•	Position Exit Worker: This worker listens for exit signals based on certain conditions (like stop-loss, take-profit, or other criteria) and manages the closing of positions.

The goal of this system is to simulate the behavior of a distributed trading bot capable of running multiple tasks asynchronously while maintaining synchronization through ZeroMQ.

Features

	•	Real-Time Data Streaming: The system uses ZeroMQ Pub/Sub to stream real-time market data and trading signals to multiple worker processes.
	•	Scalable: Multiple workers can be added to scale the system for different tasks, such as order entry, risk management, and backtesting.
	•	Modular Design: The system is designed with modular components, making it easy to extend with additional features, such as risk management strategies or more advanced algorithms.

Architecture Diagram

       +-------------------+ 
       |                   | 
       |      Server       |  <----->  (ZeroMQ PUB)
       |  (Trading Algo)   | 
       |                   |
       +--------+----------+
                |
        +-------+-------+     +----------------+
        |               |     |                |
        |  Position     |     |  Position      |
        |  Enter Worker |     |  Exit Worker   |
        |               |     |                |
        +---------------+     +----------------+

Key Components

	1.	Server (Publisher):
	•	Fetches real-time market data.
	•	Processes trading signals using algorithms.
	•	Publishes buy/sell signals to workers via ZeroMQ PUB socket.
	2.	Workers (Subscribers):
	•	Position Enter Worker: Listens for signals to enter new positions.
	•	Position Exit Worker: Listens for signals to close positions based on exit conditions.
	3.	ZeroMQ:
	•	Publish/Subscribe (PUB/SUB) pattern for communication between the server and workers.
	•	Lightweight and fast messaging system designed for real-time data streaming.

Requirements

	•	Python 3.6+ for the server
	•	Rust for worker applications
	•	ZeroMQ library for Python: pyzmq
	•	ZeroMQ library for Rust: zmq
	•	Real-time market data API (e.g., from exchanges like Binance, Coinbase Pro, etc.)

Setup

1. Install Dependencies

Python:

Install the necessary Python packages via pip:

pip install pyzmq numpy pandas torch

Rust:

Make sure you have the zmq crate in your Cargo.toml for ZeroMQ functionality:

[dependencies]
zmq = "0.10"

2. ZeroMQ Installation

Ensure that ZeroMQ is installed on your machine. For macOS, you can use Homebrew:

brew install zmq

For Windows and Linux, you can download the binaries or install via package managers (e.g., apt, pacman).

3. Running the System

Start the Server (Publisher):

Run the server script to start publishing market data and trading signals:

python server.py

Start the Workers (Subscribers):

Run the worker scripts on different machines (or the same machine) to subscribe to the signals from the server:

cargo run --release --bin position-enter-worker
cargo run --release --bin position-exit-worker

Each worker listens to the server’s signals and takes action based on the task assigned.

Usage

	1.	The server continuously fetches live market data and processes trading signals.
	2.	The workers, subscribed to the relevant channels, take action based on the signals:
	•	The Position Enter Worker will open new trades when a buy signal is received.
	•	The Position Exit Worker will close positions when the conditions for exit (such as stop loss or profit targets) are met.

Example Signals

	•	Buy Signal: A signal to enter a long position.
	•	Sell Signal: A signal to enter a short position.
	•	Exit Signal: A signal to close an open position.

These signals are published to the ZeroMQ channels, where the workers can listen and act accordingly.

How It Works

	1.	ZeroMQ PUB/SUB Communication:
	•	The Server sends out trading signals (e.g., “Buy ETH”, “Sell BTC”) over a ZeroMQ publish socket.
	•	The Workers (subscribers) listen for these signals, process them, and execute their respective tasks (entering or exiting positions).
	2.	Real-Time Market Data:
	•	The server uses an API to fetch live market data (OHLCV data).
	•	The server uses these data to generate buy/sell signals through trading algorithms (e.g., using moving averages, momentum indicators).
	3.	Modular Workers:
	•	The system allows you to add more workers to handle different aspects of the trading workflow, such as risk management, logging, and backtesting.

Future Work

	•	Risk Management: Implement a worker that subscribes to signals and manages risk, including setting stop-loss and take-profit orders.
	•	Backtesting: Implement a backtest mode where the server can simulate trading signals and calculate the performance of strategies over historical data.
	•	Multi-Exchange Support: Expand the system to support multiple exchanges, fetching data and placing orders across different platforms.

