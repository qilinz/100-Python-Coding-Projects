import os
from twilio.rest import Client


class NotificationManager:
    # This class is responsible for sending notifications with the deal flight details.
    def __init__(self):
        self.account = os.environ["TWILIO_ACCOUNT_SID"]
        self.token = os.environ["TWILIO_AUTH_TOKEN"]
        self.number = os.environ["TWILIO_NUMBER"]

    def send_message(self, text):
        client = Client(self.account, self.token)
        message = client.messages \
            .create(
                body=text,
                from_=self.number,
                to='+33643648285',
            )

        print(message.sid)
