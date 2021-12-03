import requests
import os
from datetime import datetime

pixela_endpoint = "https://pixe.la/v1/users"
USERNAME = os.environ['PIXELA_USER_2']
TOKEN = os.environ['PIXELA_TOKEN']

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# # STEP 1: create a user
# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)
# # https://pixe.la/@chestnnut

# STEP 2: create a graph
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": "graph1",
    "name": "Reading Graph",
    "unit": "page",
    "type": "int",
    "color": "kuro",
}

headers = {
    "X-USER-TOKEN": TOKEN,
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)
## https://pixe.la/v1/users/chestnnut/graphs/graph1.html

# STEP 3: post value to the graph
value_endpoint = f"{graph_endpoint}/graph1"

date_to_record = datetime.now()
value_config = {
    "date": date_to_record.strftime("%Y%m%d"),
    "quantity": input("How many pages have you read today?")
}

response = requests.post(url=value_endpoint, json=value_config, headers=headers)
print(response.text)

# OPTIONAL STEP 1: update the graph
## update the unit to "pages"
graph_update_config = {
    "unit": "pages",
}

# response = requests.put(url=value_endpoint, json=graph_update_config, headers=headers)
# print(response.text)

# OPTIONAL STEP 2: delete a record
data_delete_endpoint = f"{value_endpoint}/20211202"

# response = requests.delete(url=data_delete_endpoint, headers=headers)
# print(response)