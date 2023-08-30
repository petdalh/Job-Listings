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
    conn.close()

if __name__ == "__main__":
    setup_database()

