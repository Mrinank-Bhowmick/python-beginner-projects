import sqlite3


def create_database():
    # Connect to the SQLite database (it will create the file if it doesn't exist)
    conn = sqlite3.connect("quiz_game.db")

    # Create a cursor object
    cursor = conn.cursor()

    # Create a table to store players' scores
    cursor.execute(
        """
    CREATE TABLE IF NOT EXISTS scores (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        score INTEGER NOT NULL,
        timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
    )
    """
    )

    # Commit the changes and close the connection
    conn.commit()
    conn.close()

    print("Database and table created successfully.")


if __name__ == "__main__":
    create_database()
