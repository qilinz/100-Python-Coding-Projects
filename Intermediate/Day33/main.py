import requests
from datetime import datetime
import re
import smtplib
import time

# fill in the info indicating where you are
LATITUDE = 48.8611473
LONGITUDE = 2.3380277

# fill in your email info to send email. (need to change email security setting)
EMAIL = "YOUR_EMAIL"
PASSWORD = "YOUR_PASSWORD"


def iss_is_above():
    # get iss current position
    iss_response = requests.get("http://api.open-notify.org/iss-now.json")
    iss_response.raise_for_status()
    iss_data = iss_response.json()
    iss_long = float(iss_data["iss_position"]["longitude"])
    iss_lat = float(iss_data["iss_position"]["latitude"])
    # check if the iss is near the given location
    if abs(iss_long - LONGITUDE) <= 5 and abs(iss_lat - LATITUDE) <= 5:
        return True


def is_night():
    # get the sunrise/ sunset time for given location
    parameters = {
        "lat": LATITUDE,
        "lng": LONGITUDE,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()

    data = response.json()
    sunrise = data["results"]["sunrise"]
    sunset = data["results"]["sunset"]

    sunrise_hour = int(re.search(r".+T(\d+):.+", sunrise).group(1))
    sunset_hour = int(re.search(r".+T(\d+):.+", sunset).group(1))
    print(sunrise_hour, sunset_hour)
    time_now_hour = datetime.now().hour
    # if it's dark
    if time_now_hour >= sunset_hour or time_now_hour <= sunrise_hour:
        return True


def send_email():
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=EMAIL, password=PASSWORD)
        connection.sendmail(
            from_addr=EMAIL,
            to_addrs=EMAIL,
            msg="Subject:Look up!\n\n ISS is above!"
        )


# Check every hour
while True:
    time.sleep(3600)
    if iss_is_above() and is_night():
        send_email()