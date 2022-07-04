class NotificationManager:
    def send_notification(self, price, departure_city_name, departure_airport_IATA_code, arrival_city_name,
                          arrival_airport_IATA_code, outbound_date, inbound_date):
        print(f"Low Price alert! Only {price} to fly from {departure_city_name}-{departure_airport_IATA_code}"
              f" to {arrival_city_name}-{arrival_airport_IATA_code}, from {outbound_date} to {inbound_date}.")
