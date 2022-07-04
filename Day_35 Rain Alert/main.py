import requests
from twilio.rest import Client

api_key = "3035bef9a3d4e38327b77c211092e0d9"
account_sid = "ACbdb95813d830297045c867a7f4c820ec"
auth_token = "693b5e4bd2906c1f2e32bc4b35055c47"

parameters = {"lat": 51.507351,
              "lon": -0.127758,
              "appid": api_key,
              "exclude": ["current,minutely,daily"]
    }

response = requests.get(url="https://api.openweathermap.org/data/2.5/onecall", params=parameters, )
response.raise_for_status()
weather_data = response.json()["hourly"][slice(0,13)]
will_rain = False
for i in weather_data:
    if i["weather"][0]["id"] <700:
        will_rain = True
if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="It's going to rain today. Remember to bring an umbrella",
        from_='+19123781162',
        to= "+543493495168"
    )
    print(message.status)
