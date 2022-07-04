import requests
import datetime

PIXELA_ENDPOINT = "https://pixe.la/v1/users"
USERNAME = "dulckan"
TOKEN = "asdwkdicjfmg"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# response = requests.post(url=PIXELA_ENDPOINT, json=user_params)
# print(response.text)

# ---------------------------------------------------------
graph_endpoint = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs"

graph_config = {
    "id": "graph1",
    "name": "Cycling Graph",
    "unit": "Km",
    "type": "float",
    "color": "momiji"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# response =  requests.post(url=graph_endpoint, json=graph_config, headers=headers)

# ---------------------------------------------------------
today = datetime.datetime.now().strftime("%Y%m%d")

pixel_endpoint = f"{graph_endpoint}/graph1"

pixel_config = {
    "date": today,
    "quantity": "15"
}

# response_pixel = requests.post(url=pixel_endpoint, json=pixel_config, headers=headers)
# print(response_pixel.text)

# ---------------------------------------------------------

pixel_update_endpoint = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/graph1/{today}"

pixel_update_config = {
    "quantity": "37",
}

# response_update_pixel = requests.put(url=pixel_update_endpoint, json=pixel_update_config, headers=headers)
# print(response_update_pixel.text)

# ---------------------------------------------------------
pixel_delete_endpoint = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/graph1/{today}"

response_delete_pixel = requests.delete(url=pixel_delete_endpoint, headers=headers)
print(response_delete_pixel.text)
