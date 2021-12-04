import os
from twilio.rest import Client
import smtplib


class NotificationManager:
    # This class is responsible for sending notifications with the deal flight details.
    def __init__(self):
        self.account = os.environ["TWILIO_ACCOUNT_SID"]
        self.token = os.environ["TWILIO_AUTH_TOKEN"]
        self.number = os.environ["TWILIO_NUMBER"]
        self.my_email = os.environ["GMAIL"]
        self.my_password = os.environ["GMAIL_KEY"]

    def send_sms(self, text):
        client = Client(self.account, self.token)
        message = client.messages \
            .create(
                body=text,
                from_=self.number,
                to='+33643648285',
            )

        print(message.sid)

    def send_email(self, text, email):
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(
                user=self.my_email,
                password=self.my_password
            )
            connection.sendmail(
                from_addr=self.my_email,
                to_addrs=email,
                msg=f"Subject:Great Flight Deals!\n\n{text}".encode('utf-8')
            )