import requests
import os
from datetime import datetime
import json

# INFOS
GENDER = "YOUR GENDER"
WEIGHT_KG = "YOUR WEIGHT"
HEIGHT_CM = "YOUR HEIGHT"
AGE = "YOUR AGE"

# STEP 1: use Nutritionix API to process inputs
nutri_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
nutri_id = os.environ["NUTRI_ID"]
nutri_key = os.environ["NUTRI_KEY"]

nutri_headers = {
    "x-app-id": nutri_id,
    "x-app-key": nutri_key,
}

exercise_input = input("What did you do for exercising? Please specify the duration. \n")

nutri_params = {
    "query": exercise_input,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE,
}


response = requests.post(url=nutri_endpoint, json=nutri_params, headers=nutri_headers)
results = response.json()
# # check the structure
# with open("nutri_data.json", "w") as file:
#     json.dump(results, file, indent=4)


# STEP 2: put the nutri response to google sheet by sheety
# sheety API
sheety_endpoint = os.environ["SHEETY_ENDPOINT"]
sheety_token = os.environ["SHEETY_TOKEN"]
sheety_headers = {
    "Authorization": f"Bearer {sheety_token}"
}

# format the datetime
today = datetime.now()
today_date = today.strftime("%d/%m/%Y")
today_time = today.strftime("%H:%M:%S")

exercises = results["exercises"]

for exercise in exercises:
    # format the exercise
    name = exercise["name"].title()
    duration = exercise["duration_min"]
    calories = exercise["nf_calories"]

    exercise_params = {
        "workout": {
            "date": today_date,
            "time": today_time,
            "exercise": name,
            "duration": duration,
            "calories": calories,
        }
    }

    response = requests.post(url=sheety_endpoint, json=exercise_params, headers=sheety_headers)
    print(response)