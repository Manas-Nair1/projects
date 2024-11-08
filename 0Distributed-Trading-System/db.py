import sqlite3
import json
import redis
import datetime

# SQLite Setup
def create_db():
    conn = sqlite3.connect('positions.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS open_positions (
            position_id INTEGER PRIMARY KEY,
            symbol TEXT NOT NULL,
            side TEXT NOT NULL,  -- "long" or "short"
            quantity REAL NOT NULL,
            entry_price REAL NOT NULL,
            timestamp TEXT NOT NULL
        )
    ''')
    conn.commit()  # Save changes
    conn.close()

# SQLite Insert Position
def insert_position(symbol, side, quantity, entry_price):
    timestamp = datetime.datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')
    conn = sqlite3.connect('positions.db')
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO open_positions (symbol, side, quantity, entry_price, timestamp)
        VALUES (?, ?, ?, ?, ?)
    ''', (symbol, side, quantity, entry_price, timestamp))
    conn.commit()
    conn.close()

# SQLite Fetch Positions
def get_open_positions():
    conn = sqlite3.connect('positions.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM open_positions')
    positions = cursor.fetchall()
    conn.close()
    return positions

# SQLite Close Position
def close_position(position_id):
    conn = sqlite3.connect('positions.db')
    cursor = conn.cursor()
    cursor.execute('DELETE FROM open_positions WHERE position_id = ?', (position_id,))
    conn.commit()
    conn.close()

# Redis Setup
r = redis.Redis(host='localhost', port=6379, db=0)

# Redis Insert Position
def add_position_redis(position_id, symbol, side, quantity, entry_price):
    position = {
        'symbol': symbol,
        'side': side,
        'quantity': quantity,
        'entry_price': entry_price,
        'timestamp': datetime.datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')
    }
    r.set(f"position:{position_id}", json.dumps(position))

# Redis Get Position
def get_position_redis(position_id):
    position_data = r.get(f"position:{position_id}")
    if position_data:
        return json.loads(position_data)
    return None

# Main logic to run the functions
if __name__ == '__main__':
    create_db()  # Initialize SQLite DB
    
    # Example of adding a position using SQLite
    insert_position('ETHUSDT', 'long', 1.5, 3500.00)
    print("Positions in SQLite:", get_open_positions())
    
    # Example of adding a position using Redis
    add_position_redis(1, 'BTCUSDT', 'short', 0.5, 45000.00)
    print("Position in Redis:", get_position_redis(1))

    # Close a position in SQLite
    close_position(1)
    print("Positions in SQLite after closing:", get_open_positions())