from twilio.rest import Client
import os

account_sid = os.environ["TWILIO_ACCOUNT_SID"]
auth_token = os.environ["TWILIO_AUTH_TOKEN"]

client = Client(account_sid, auth_token)

def send_sms(receiver, sender, message):

    message = client.messages.create(
        to=f"+1{receiver}", 
        from_=f"+1{sender}",
        body=message)

    print(message.sid)