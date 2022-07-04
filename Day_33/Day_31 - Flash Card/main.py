from tkinter import *
from pandas import *
from random import choice

current_card = {}

try:
    data = read_csv("data/words_to_learn.csv")
    dic_data = data.to_dict(orient="records")
except FileNotFoundError:
    data = read_csv("data/french_words.csv")
    dic_data = data.to_dict(orient="records")


# ------------------------------CREATE NEW FLASH CARD----------------------------------- #


def right():
    dic_data.remove(current_card)
    next_card()
    dataframe = DataFrame(dic_data)
    dataframe.to_csv("data/words_to_learn.csv", index=False)


def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = choice(dic_data)
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(background, image=background_image)
    flip_timer = window.after(3000, solution)


def solution():
    canvas.itemconfig(background, image=background_image_back)
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")


# ------------------------------UI SETUP----------------------------------- #

BACKGROUND_COLOR = "#B1DDC6"

# Window
window = Tk()
window.title("Flash Cards")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# Canvas
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
background_image = PhotoImage(file="images/card_front.png")
background_image_back = PhotoImage(file="images/card_back.png")
background = canvas.create_image(400, 263, image=background_image)
card_title = canvas.create_text(400, 150, text="French", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, text="aaa", font=("Ariel", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)


# Buttons
right_image = PhotoImage(file="images/right.png")
right_button = Button(image=right_image, bg=BACKGROUND_COLOR, highlightthickness=0, command=right)
right_button.grid(row=1, column=1)

wrong_image = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_image, bg=BACKGROUND_COLOR, highlightthickness=0, command=next_card)
wrong_button.grid(row=1, column=0)

# Labels
flip_timer = window.after(3000, solution)
next_card()

window.mainloop()