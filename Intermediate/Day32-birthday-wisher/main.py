import pandas as pd
import smtplib
import datetime as dt
from random import randint

PLACEHOLDER = "[NAME]"
my_email = "karinz9526@gmail.com"
password = "zql*123456"

# 1. Read the birthdays.csv
birthday_list = pd.read_csv("birthdays.csv")

# 2. Check if today matches a birthday in the birthdays.csv
today = dt.datetime.now()
today_month = today.month
today_day = today.day

matched_people = birthday_list.loc[(birthday_list['month'] == today_month) & (birthday_list['day'] == today_day)]
people_list = matched_people.to_dict(orient="records")

if len(people_list) > 0:
    # 3. If matched, pick a random letter and replace the [NAME] with the person's actual name from birthdays.csv
    # random choose one
    for person in people_list:
        letter_filename = f"letter_templates/letter_{randint(1,3)}.txt"

        # change the name
        with open(letter_filename) as letter_file:
            letter = letter_file.read()
            name = person['name']
            letter = letter.replace(PLACEHOLDER, name)

        # 4. Send the letter generated in step 3 to that person's email address.
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(
                from_addr=my_email,
                to_addrs=person['email'],
                msg=f"Subject:BIG DAY!\n\n{letter}"
            )