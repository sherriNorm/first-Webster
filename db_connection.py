import sqlite3

def connect_to_db(db_name):
    try:
        # Establish connection to SQLite database (or create it if it doesn't exist)
        conn = sqlite3.connect(db_name)
        print(f"Connected to database: {db_name}")
        return conn
    except sqlite3.Error as e:
        print(f"Error connecting to database: {e}")
        return None

# Example usage
if __name__ == "__main__":
    db_name = 'my_database.db'
    connection = connect_to_db(db_name)
    if connection:
        connection.close()
