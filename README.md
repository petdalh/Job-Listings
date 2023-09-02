# Job Scraper with SMS Notifications

## Overview

This project is a web scraper that fetches job listings from a specific website and stores them in a SQLite database. If a new job is found that isn't already in the database, the script sends an SMS notification using Twilio.

## Prerequisites

- Python 3.x
- SQLite
- A Twilio account

## Setup

### Clone the Repository

First, clone the repository to your local machine:

\\\bash
git clone <repository_url>
\\\

### Create a Virtual Environment (Optional)

It's a good practice to create a virtual environment:

\\\bash
python3 -m venv venv
source venv/bin/activate  # On Windows, use \`venv\\Scripts\\activate\`
\\\

### Install Dependencies

Install the required Python packages:

\\\bash
pip install requests
pip install beautifulsoup4
pip install twilio
pip install python-dotenv
\\\

### Twilio Account Setup

1. Create a new Twilio account or sign in to your existing account.
2. Obtain your \`ACCOUNT SID\` and \`AUTH TOKEN\`.
3. Get a Twilio phone number.

### Environment Variables

Create a .env file in the project root directory and add the following content:


TWILIO_ACCOUNT_SID=your_account_sid_here
TWILIO_AUTH_TOKEN=your_auth_token_here
TWILIO_PHONE_NUMBER=your_twilio_phone_number_here
MY_PHONE_NUMBER=your_personal_phone_number_here


Replace the placeholders with the actual values from your Twilio account.

## Running the Script

To run the script, navigate to the project directory and execute:

\\\bash
python main_script.py  # Replace 'main_script.py' with the actual name of your script
\\\

## How It Works

1. The script scrapes job listings from the specified website.
2. It checks if each job is already in the SQLite database.
3. If a new job is found, it's added to a list.
4. After all jobs have been checked, an SMS is sent containing all the new jobs found.

## How It Looks

![Application Workflow](IMG_4803./.png)


