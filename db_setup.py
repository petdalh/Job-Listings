import sqlite3

def setup_database():
    conn = sqlite3.connect('job_listings.db')
    conn.execute('''
    CREATE TABLE IF NOT EXISTS JOBS
    (ID INTEGER PRIMARY KEY AUTOINCREMENT,
    URL TEXT UNIQUE NOT NULL,
    TYPE TEXT NOT NULL,
    TITLE TEXT NOT NULL,
    DEADLINE TEXT NOT NULL,
    LOGO_URL TEXT NOT NULL);
    ''')
    
    # Add the SOURCE column if it doesn't exist
    try:
        conn.execute("ALTER TABLE JOBS ADD COLUMN SOURCE TEXT NOT NULL;")
    except sqlite3.OperationalError as e:
        print(e)  # Column already exists or other OperationalError
    
    conn.close()


if __name__ == "__main__":
    setup_database()