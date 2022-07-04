# from twilio.rest import Client
import requests
import smtplib
#
# TWILIO_SID = "ACbdb95813d830297045c867a7f4c820ec"
# TWILIO_AUTH_TOKEN = "693b5e4bd2906c1f2e32bc4b35055c47"
# TWILIO_VIRTUAL_NUMBER = '+19123781162'
# TWILIO_VERIFIED_NUMBER = "+543493495168"
#
#
class NotificationManager:
#
#     def __init__(self):
#         self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)
#
#     def send_sms(self, message):
#         message = self.client.messages.create(
#             body=message,
#             from_=TWILIO_VIRTUAL_NUMBER,
#             to=TWILIO_VERIFIED_NUMBER,
#         )
#         # Prints if successfully sent.
#         print(message.sid)


        def send_email(self,msg):
            MY_EMAIL = "franco.galli049@gmail.com"
            PASSWORD = "telefono"

            SHEETY_ENDPOINT_GET = "https://api.sheety.co/e7f0964482a12e6908560ff843fb769f/flightDeals/users"

            response = requests.get(url=SHEETY_ENDPOINT_GET)
            response.raise_for_status()
            data = response.json()["users"]
            for i in data:
                with smtplib.SMTP("smtp.gmail.com") as connection:
                    connection.starttls()
                    connection.login(user=MY_EMAIL, password=PASSWORD)
                    connection.sendmail(
                        from_addr=MY_EMAIL,
                        to_addrs=i["email"],
                        msg=msg
                    )