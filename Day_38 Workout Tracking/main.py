import requests
import datetime
import os

APP_ID = os.environ.get("APP_ID")
API_KEY = os.environ.get("API_KEY")



NUTRITIONIX_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"
SHEETY_ENDPOINT_ADD_A_ROW = os.environ.get("SHEETY_ENDPOINT_ADD_A_ROW")

AUTH_SHEETU = os.environ.get("AUTH_SHEETU")

header_nutritionix = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY
}

query = input("Tell me which exercises you did: ")

parameters_nutritionix = {
    "query": query,
    "gender": "male",
    "weight_kg": "75",
    "height_cm": "180",
    "age": "29"
}

response_sheety = requests.post(
    url=NUTRITIONIX_ENDPOINT,
    json=parameters_nutritionix,
    headers=header_nutritionix)
data = response_sheety.json()

#-----------------------------------------------------------------------------------------------------------------------

now = datetime.datetime.now().strftime("%d/%m/%Y")
time = datetime.datetime.now().strftime("%X")

for exercise in data["exercises"]:
    parameters_sheety = {
        "workout": {
            "date": now,
            "time": time,
            "exercise": exercise["name"],
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
}
    response_sheety = requests.post(
        url=SHEETY_ENDPOINT_ADD_A_ROW,
        json=parameters_sheety,
        headers={"Authorization": AUTH_SHEETU})
    print(response_sheety.text)