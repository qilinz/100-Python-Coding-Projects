from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager
from datetime import date, timedelta

# start place of the flights
FLY_FROM = "LON"


flight_search = FlightSearch()
data_manager = DataManager()
notification_manager = NotificationManager()
plan_data = data_manager.get_record()

# ----------------- Find the missing IATA code for cities on Google sheets --------------------#
for record in plan_data:
    if record["iataCode"] == "":
        record["iataCode"] = flight_search.search_code(record["city"])
        data_manager.update_record(record)

# --------------- Search the cheapest price -------------------_#
# travel date: tomorrow - 6 months max
tomorrow = date.today() + timedelta(days=1)
end_date = tomorrow + timedelta(days=180)

message_text = ""
for record in plan_data:
    flight_data = flight_search.check_flight(
        start_place=FLY_FROM,
        end_place=record["iataCode"],
        from_date=tomorrow,
        end_date=end_date
    )
    if (flight_data is not None) and (flight_data.price < record["lowestPrice"]):
        message_text += f"\nOnly £ {flight_data.price} for {flight_data.to_city} trip!" \
                        f"\n  {flight_data.out_date} to {flight_data.return_date}"
    else:
        print(f"No cheaper flight for {record['city']}.")

if len(message_text) > 0:
    notification_manager.send_message(message_text)