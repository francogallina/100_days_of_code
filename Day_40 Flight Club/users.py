import requests

SHEETY_ENDPOINT_POST = "https://api.sheety.co/e7f0964482a12e6908560ff843fb769f/flightDeals/users"

while True:
    print("Welcome to Franco's Flight Club.")
    print("We find the best flight deals and email you")
    name = input("What is your first name? ")
    last_name = input("What is your last name? ")
    email = input("What is your email? ")
    re_email = input("Type your email again: ")

    if name != "" and last_name != "" and email == re_email:
        data = {
            "user":{
                "firstName": name,
                "lastName": last_name,
                "email": email
        }}
        post = requests.post(url=SHEETY_ENDPOINT_POST, json=data)
    else:
        print("Error!!")
