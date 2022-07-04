from tkinter import *
from pandas import *
from random import choice
import time

data = read_csv("data/french_words.csv")
dic_data = data.to_dict(orient="records")

print(dic_data)