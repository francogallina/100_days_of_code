import smtplib
import datetime as dt
from random import choice

my_email = "franco.galli049@gmail.com"
password = "telefono"

with open("quotes.txt") as data:
    data_list = data.readlines()

random_quotes = choice(data_list)

day = dt.datetime.now()
day_week = day.weekday()
if day_week == 1:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs= "prueba.python@yahoo.com",
            msg= f"Subject:Quotes\n\n{random_quotes}"
        )



# now = dt.datetime.now()
# year = now.year
# date_of_birth = dt.datetime(year=1995, month=12, day=15)
# print(date_of_birth)