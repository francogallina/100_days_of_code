from tkinter import *
from tkinter import messagebox, Label
import random
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def random_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters = [random.choice(letters) for _ in range(nr_letters)]
    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]

    password_list = password_letters + password_symbols + password_numbers

    random.shuffle(password_list)

    password_g = "".join(password_list)
    password_entry.insert(0, password_g)
    pyperclip.copy(password_g)
# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():

    website_text = (website_entry.get()).lower()
    email_text = (email_entry.get()).lower()
    password_text = password_entry.get()
    new_data ={
        website_text: {
            "email": email_text,
            "password": password_text

        }
    }

    if len(website_text) < 1 or len(password_text) < 1:
        messagebox.showinfo(title="Error", message="Invalid website or password")
    else:
        try:
            with open("data.json", "r") as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            data.update(new_data)

            with open("data.json", "w") as data_file:
                json.dump(data, data_file, indent=4)
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)

# ---------------------------- FIND PASSWORD ------------------------------- #

def find_password():
    search = (website_entry.get()).lower()
    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
    except (FileNotFoundError, KeyError):
        messagebox.showinfo(title="Error", message="No Data File Found.")
    else:
        if search in data:
            email_search = data[search]["email"]
            password_search = data[search]["password"]
            messagebox.showinfo(title="Info account", message=f"Email: {email_search}\nPassword: {password_search}")
        else:
            messagebox.showinfo(title="Error", message=f"No details for {search} exists.")


# ---------------------------- UI SETUP ------------------------------- #
# Window
window = Tk()
window.title("Pasword Manager")
window.config(padx=50, pady=50)

# Canvas
canvas = Canvas(width=200, height=200)
image_logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=image_logo)
canvas.grid(column=1, row=0)

# Labels
website_label = Label(text="Website:")
website_label.grid(column=0, row=1)

email_label = Label(text="Email/Username:")
email_label.grid(column=0, row=2)

password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

# Buttons
generate_password = Button(text="Generate Password", command=random_password)
generate_password.grid(column=2, row=3, sticky="EW")

add = Button(text="Add", width=37, command=save)
add.grid(column=1, row=4, columnspan=2, sticky="EW")

search_button = Button(text="Search", command=find_password)
search_button.grid(row=1, column=2, sticky="EW")

# Entries
website_entry = Entry(width=25)
website_entry.grid(column=1, row=1, sticky="EW")
website_entry.focus()

email_entry = Entry(width=43)
email_entry.grid(column=1, row=2, columnspan=2, sticky="EW")
email_entry.insert(0, "franco@hotmail.com")

password_entry = Entry(width=25)
password_entry.grid(column=1, row=3, sticky="EW")

window.mainloop()
