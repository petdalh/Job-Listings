import os
import twilio
import twilio.rest

TWILIO_ACCOUNT_SID = os.getenv("TWILIO_ACCOUNT_SID")
TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")
TWILIO_PHONE_NUMBER = os.getenv("TWILIO_PHONE_NUMBER")
MY_PHONE_NUMBER = os.getenv("MY_PHONE_NUMBER")


def send_sms(message):
    client = twilio.rest.Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

    message = client.messages.create(
        body=message,
        from_=TWILIO_PHONE_NUMBER,  # Replace with your Twilio number
        to=MY_PHONE_NUMBER  # Replace with your phone number
    )

    print(f"Message sent with SID: {message.sid}")
