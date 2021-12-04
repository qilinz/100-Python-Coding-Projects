import requests
import os
import json
from flight_data import FlightData


class FlightSearch:
    # This class is responsible for talking to the Flight Search API.
    def __init__(self):
        self.token = os.environ["TEQUILA_TOKEN"]
        self.endpoint = "https://tequila-api.kiwi.com"
        self.location_endpoint = f"{self.endpoint}/locations/query"
        self.search_endpoint = f"{self.endpoint}/v2/search"
        self.headers = {
            "apikey": self.token,
        }

    def search_code(self, city):
        params = {
            "term": city,
            "locale": "en-US",
            "location_types": "city",
            "limit": 1,
            "active_only": True,
        }
        response = requests.get(url=self.location_endpoint, params=params, headers=self.headers)
        response.raise_for_status()
        data = response.json()
        code = data["locations"][0]["code"]
        return code

    def check_flight(self, start_place, end_place, from_date, end_date):
        query = {
            "fly_from": start_place,
            "fly_to": end_place,
            "date_from": from_date.strftime("%d/%m/%Y"),
            "date_to": end_date.strftime("%d/%m/%Y"),
            "nights_in_dst_from": 2,
            "nights_in_dst_to": 30,
            "flight_type": "round",
            "curr": "GBP",
            "one_for_city": 1,
            "max_stopovers": 0,
        }
        response = requests.get(url=self.search_endpoint, params=query, headers=self.headers)
        response.raise_for_status()
        data = response.json()
        # # check date structure
        # with open("sample_data.json", "w") as file:
        #     json.dump(data, file, indent=4)

        try:
            flight_info = data["data"][0]
        except IndexError:

            # check if there's flight with max 2 stopovers for a round trip
            query["max_stopovers"] = 2
            response = requests.get(url=self.search_endpoint, params=query, headers=self.headers)
            response.raise_for_status()
            data = response.json()
            try:
                flight_info = data["data"][0]
            except IndexError:
                print(f"No flight available from {start_place} to {end_place}")
                return None
            else:
                # # check date structure
                # with open("sample_data_stopover.json", "w") as file:
                #     json.dump(data, file, indent=4)

                # return data for stopover flight
                flight_data = FlightData(
                    price=flight_info["price"],
                    from_city=flight_info["cityFrom"],
                    from_airport=flight_info["route"][0]["flyFrom"],
                    to_city=flight_info["cityTo"],
                    to_airport=flight_info["route"][1]["flyTo"],
                    out_date=flight_info["route"][0]["utc_departure"].split("T")[0],
                    return_date=flight_info["route"][1]["utc_departure"].split("T")[0],
                    stop_overs=2,
                    via_city=flight_info["route"][0]["cityTo"],
                )
                return flight_data

        # return data for direct flight
        flight_data = FlightData(
            price=flight_info["price"],
            from_city=flight_info["cityFrom"],
            from_airport=flight_info["route"][0]["flyFrom"],
            to_city=flight_info["cityTo"],
            to_airport=flight_info["route"][0]["flyTo"],
            out_date=flight_info["route"][0]["utc_departure"].split("T")[0],
            return_date=flight_info["route"][1]["utc_departure"].split("T")[0],
        )
        return flight_data