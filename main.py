from bs4 import BeautifulSoup
import requests
from db_operations import insert_job, delete_all_records, job_exists
from db_setup import setup_database
from sms_operations import send_sms

# delete_all_records()

setup_database()

base_url = "https://www.teknologiporten.no"
url = f"{base_url}/nb/stillingsannonser/"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

new_jobs = []

# Find all job listings
job_listings = soup.find_all('div', class_='adx_contain')

for job_div in job_listings:
    # Initialize variables to 'None'
    job_type = job_title = app_deadline = logo_url = job_url = 'None'
    
    # Extract job URL
    a_tag = job_div.find_parent('a', href=True)
    if a_tag:
        job_url = base_url + a_tag['href']
    
    # Extract job type
    for p in job_div.find_all('p'):
        if 'Stillingstype:' in p.text:
            job_type = p.find_next('strong').text.strip()
            break
    
    # Extract job title
    job_title_h1 = job_div.find('h1')
    if job_title_h1:
        job_title = job_title_h1.text.strip()
    
    # Extract application deadline
    for p in job_div.find_all('p'):
        if 'Søknadsfrist:' in p.text:
            app_deadline = p.find_next('strong').text.strip()
            break
    
    # Extract company logo URL
    logo_img = job_div.find('img', {'class': 'logo'})
    if logo_img:
        logo_url = logo_img['src']
    
    # Insert the scraped data into the database
        is_new_job = insert_job(job_url, job_type, job_title, app_deadline, logo_url, "Teknologiporten")
    
    # If it's a new job, send an SMS
    if is_new_job:
        new_job_info = f"New job found: {job_title} at {job_url}"
        new_jobs.append(new_job_info)

if new_jobs:
    message = "\n".join(new_jobs)
    send_sms(message)