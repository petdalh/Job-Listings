import sqlite3

def insert_job(url, job_type, title, deadline, logo_url):
    conn = sqlite3.connect('job_listings.db')
    conn.execute("INSERT OR IGNORE INTO JOBS (URL, TYPE, TITLE, DEADLINE, LOGO_URL) VALUES (?, ?, ?, ?, ?)",
                 (url, job_type, title, deadline, logo_url))
    conn.commit()
    conn.close()