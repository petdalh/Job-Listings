import os
from twilio.rest import Client
from dotenv import load_dotenv
load_dotenv()




TWILIO_ACCOUNT_SID = os.getenv("TWILIO_ACCOUNT_SID")
TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")
TWILIO_PHONE_NUMBER = os.getenv("TWILIO_PHONE_NUMBER")
MY_PHONE_NUMBER = os.getenv("MY_PHONE_NUMBER")



def send_sms(message):
    client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

    message = client.messages.create(
        body=message,
        from_=TWILIO_PHONE_NUMBER,  
        to=MY_PHONE_NUMBER  
    )

    print(f"Message sent with SID: {message.sid}")

print("Hello world")
