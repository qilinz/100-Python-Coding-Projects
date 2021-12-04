class FlightData:
    # This class is responsible for structuring the flight data.
    def __init__(self, price, from_city, from_airport, to_city, to_airport, out_date, return_date,
                 stop_overs=0, via_city=""):
        self.price = price
        self.from_city = from_city
        self.from_airport = from_airport
        self.to_city = to_city
        self.to_airport = to_airport
        self.out_date = out_date
        self.return_date = return_date
        self.stop_overs = stop_overs
        self.via_city = via_city
