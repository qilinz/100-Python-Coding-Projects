import os
import requests


def email_verification():
    email_first = input("What's your email?\n")
    email_second = input("Please type your email again.\n")
    if email_first == email_second:
        return email_first
    else:
        print("The emails are not matched. Please re-enter your email.")
        return email_verification()


# welcome message
print("Welcome to Chestnut's Flight Club."
      "\nWe can find cheaper flights and email you."
      "\nPlease sign up by filling the form:\n")

first_name = input("What's your first name?\n")
last_name = input("What's your last name?\n")
email = email_verification()
print(email)

# sheety info
endpoint = "https://api.sheety.co/bad8666ff819f78c153b8f3589d70122/flightDeals/users"
token = os.environ["SHEETY_TOKEN"]
headers = {
    "Authorization": f"Bearer {token}"
}
user_info = {
    "user": {
        "firstName": first_name,
        "lastName": last_name,
        "email": email,
    }
}
response = requests.post(
    url=endpoint,
    json=user_info,
    headers=headers,
)
response.raise_for_status()
status = response.status_code

if status == 200:
    print("Thanks for signing up! You're in the club! We will email you best deals :)")


