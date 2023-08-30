import sqlite3

def setup_database():
    conn = sqlite3.connect('job_listings.db')
    c = conn.cursor()
    
    # Create table if it doesn't exist
    c.execute('''
    CREATE TABLE IF NOT EXISTS JOBS
    (ID INTEGER PRIMARY KEY AUTOINCREMENT,
    URL TEXT UNIQUE NOT NULL,
    TYPE TEXT NOT NULL,
    TITLE TEXT NOT NULL,
    DEADLINE TEXT NOT NULL,
    LOGO_URL TEXT NOT NULL);
    ''')
    
    # Check if the SOURCE column exists
    c.execute("PRAGMA table_info(JOBS);")
    columns = [column[1] for column in c.fetchall()]
    
    if 'SOURCE' not in columns:
        try:
            c.execute("ALTER TABLE JOBS ADD COLUMN SOURCE TEXT DEFAULT 'Unknown';")
        except sqlite3.OperationalError as e:
            print(f"An error occurred: {e}")
    
    conn.commit()
    conn.close()

if __name__ == "__main__":
    setup_database()