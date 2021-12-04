######## using sheety API to process data in Google docs
import requests
import os


class DataManager:
    def __init__(self):
        self.endpoint = "https://api.sheety.co/bad8666ff819f78c153b8f3589d70122/flightDeals"
        self.token = os.environ['SHEETY_TOKEN']
        self.headers = {
            "Authorization": f"Bearer {self.token}"
        }

    def get_record(self):
        response = requests.get(url=f"{self.endpoint}/prices", headers=self.headers)
        data = response.json()
        return data['prices']

    def update_record(self, city_dict):
        city_id = city_dict["id"]
        city_endpoint = f"{self.endpoint}/prices/{city_id}"
        city_dict.pop("id")
        city_info = {
            "price": city_dict
        }
        response = requests.put(url=city_endpoint, json=city_info, headers=self.headers)
        response.raise_for_status()

    def get_user(self):
        response = requests.get(url=f"{self.endpoint}/users", headers=self.headers)
        data = response.json()
        return data['users']