import sqlite3

def insert_job(url, job_type, title, deadline, logo_url, source):
    conn = sqlite3.connect('job_listings.db')
    cursor = conn.cursor()
    cursor.execute("INSERT OR IGNORE INTO JOBS (URL, TYPE, TITLE, DEADLINE, LOGO_URL, SOURCE) VALUES (?, ?, ?, ?, ?, ?)",
                 (url, job_type, title, deadline, logo_url, source))
    is_new_job = cursor.rowcount == 1  # True if a new job is inserted
    conn.commit()
    conn.close()
    return is_new_job


def delete_all_records():
    # Connect to the SQLite database
    conn = sqlite3.connect('job_listings.db')
    
    # Create a cursor object to execute SQL queries
    cursor = conn.cursor()
    
    # Delete all records from the JOBS table
    cursor.execute("DELETE FROM JOBS")
    
    # Commit the changes
    conn.commit()
    
    # Close the database connection
    conn.close()
    
def job_exists(url):
    conn = sqlite3.connect('job_listings.db')
    cursor = conn.cursor()
    cursor.execute("SELECT 1 FROM JOBS WHERE URL=?", (url,))
    exists = cursor.fetchone()
    conn.close()
    return exists is not None