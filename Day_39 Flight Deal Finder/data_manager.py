import requests

SHEETY_ENDPOINT_GET = "https://api.sheety.co/e7f0964482a12e6908560ff843fb769f/flightDeals/prices"


class DataManager:
    def __init__(self):
        self.destination_data = {}

    def get_destination_data(self):
        response = requests.get(url=SHEETY_ENDPOINT_GET)
        response.raise_for_status()
        data = response.json()
        return data["prices"]

    def update_destination_code(self):
        for i in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": i["iataCode"]
                }
            }
            update_sheet = requests.put(
                url= f"{SHEETY_ENDPOINT_GET}/{i['id']}",
                json= new_data
            )
            print(update_sheet)

