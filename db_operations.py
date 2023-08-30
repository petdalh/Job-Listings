import sqlite3

def insert_job(url, job_type, title, deadline, logo_url, source):
    conn = sqlite3.connect('job_listings.db')
    conn.execute("INSERT OR IGNORE INTO JOBS (URL, TYPE, TITLE, DEADLINE, LOGO_URL, SOURCE) VALUES (?, ?, ?, ?, ?, ?)",
                 (url, job_type, title, deadline, logo_url, source))
    conn.commit()
    conn.close()


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

# Call the function to delete all records
delete_all_records()