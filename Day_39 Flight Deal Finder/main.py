from data_manager import DataManager
import datetime
from flight_search import FlightSearch
from notification_manager import NotificationManager

data_manager = DataManager()
sheet_data = data_manager.get_destination_data()
flight_search = FlightSearch()
notification_manager = NotificationManager()

ORIGIN_CITY_IATA = "LON"

if sheet_data[0]["iataCode"] == "":
    for i in sheet_data:
        i["iataCode"] = flight_search.get_destination_code(i["city"])
    data_manager.destination_data = sheet_data
    data_manager.update_destination_code()

now = datetime.datetime.now() + datetime.timedelta(days=1)
six_months = datetime.datetime.now() + datetime.timedelta(days=180)

for i in sheet_data:
    flight = flight_search.check_flights(
        ORIGIN_CITY_IATA,
        i["iataCode"],
        from_time=now,
        to_time=six_months
    )
    try:
        if i["lowestPrice"] >= flight.price:
            notification_manager.send_notification(flight.price, flight.origin_city, flight.origin_airport,
                                                   flight.destination_city, flight.destination_airport, flight.out_date,
                                                   flight.return_date)
    except AttributeError:
        pass

