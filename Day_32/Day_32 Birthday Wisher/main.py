from pandas import *
import datetime as dt
from random import choice
import smtplib

my_email = "franco.galli049@gmail.com"
password = "telefono"


now = dt.datetime.now()
current_month = now.month
current_day = now.day

list_letters = ["letter_templates/letter_1.txt", "letter_templates/letter_2.txt", "letter_templates/letter_3.txt"]

data_brithday = read_csv("birthdays.csv")
birthday_to_dict = data_brithday.to_dict(orient="records")
for i in range(len(birthday_to_dict)):
    if birthday_to_dict[i]["day"] == current_day and birthday_to_dict[i]["month"] == current_month:
        random_letter = choice(list_letters)
        with open(random_letter) as letter:
            text = letter.read()
        text_replace = text.replace("[NAME]", birthday_to_dict[i]["name"])
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(
                from_addr=my_email,
                to_addrs="prueba.python@yahoo.com",
                msg=text_replace
            )


# from datetime import datetime
# import pandas
# import random
# import smtplib
#
# MY_EMAIL = "YOUR EMAIL"
# MY_PASSWORD = "YOUR PASSWORD"
#
# today = datetime.now()
# today_tuple = (today.month, today.day)
#
# data = pandas.read_csv("birthdays.csv")
# birthdays_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}
# if today_tuple in birthdays_dict:
#     birthday_person = birthdays_dict[today_tuple]
#     file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"
#     with open(file_path) as letter_file:
#         contents = letter_file.read()
#         contents = contents.replace("[NAME]", birthday_person["name"])
#
#     with smtplib.SMTP("YOUR EMAIL PROVIDER SMTP SERVER ADDRESS") as connection:
#         connection.starttls()
#         connection.login(MY_EMAIL, MY_PASSWORD)
#         connection.sendmail(
#             from_addr=MY_EMAIL,
#             to_addrs=birthday_person["email"],
#             msg=f"Subject:Happy Birthday!\n\n{contents}"
#         )

