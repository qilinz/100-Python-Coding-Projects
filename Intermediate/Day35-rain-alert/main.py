import requests
import json
import os
from twilio.rest import Client

# open weather API key
owm_api = os.environ["OWM_API_KEY"]

# rain alert message
alert_message = "It's rainy today. Please take an umbrella."

# number where you want to send the alert
alert_number = "YOUR ALERT NUMBER"

# the location you would like to check (current input is Paris)
LAT = 48.856613
LONG = 2.352222

# parameters for open weather API
parameters = {
    "lat": LAT,
    "lon": LONG,
    "appid": owm_api,
}

response = requests.get(url="https://api.openweathermap.org/data/2.5/onecall", params=parameters)
response.raise_for_status()

# save the weather data
data = response.json()
hour_data = data["hourly"]

# save as json to check the structure
# with open("weather_data.json", "w") as file:
#     json.dump(data, file, indent=4)


def is_rainy():
    """
    Check if there's rain or snow in the following 12 hours
    """
    for hour_weather in hour_data[:12]:
        condition_code = hour_weather["weather"][0]["id"]
        # < 700 means rains and snow
        if int(condition_code) < 700:
            return True


# if it rains, send an alert
if is_rainy():

    # set up the twilio service
    account_sid = os.environ['TWILIO_ACCOUNT_SID']
    auth_token = os.environ['TWILIO_AUTH_TOKEN']
    twilio_number = os.environ['TWILIO_NUMBER']

    client = Client(account_sid, auth_token)

    # sent the message
    message = client.messages \
                    .create(
                         body=alert_message,
                         from_=twilio_number,
                         to=alert_number
                     )

    # check the status
    print(message.status)