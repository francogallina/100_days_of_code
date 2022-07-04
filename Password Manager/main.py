from tkinter import *
from tkinter import messagebox, Label
import random
import pyperclip

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
    website_text = website_entry.get()
    email_text = email_entry.get()
    password_text = password_entry.get()
    if len(website_text) < 1 or len(password_text) < 1:
        messagebox.showinfo(title="Error", message="Invalid website or password")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {email_text}"
                                                              f"\nPassword:{password_text}\nIs it ok to save? ")
        if is_ok:
            with open("data.txt", "a") as data_file:
                data_file.write(f"{website_text} | {email_text} | {password_text}\n")
                website_entry.delete(0, END)
                password_entry.delete(0, END)


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
website: Label = Label(text="Website:")
website.grid(column=0, row=1)

email = Label(text="Email/Username:")
email.grid(column=0, row=2)

password = Label(text="Password:")
password.grid(column=0, row=3)

# Buttons
generate_password = Button(text="Generate Password", command=random_password)
generate_password.grid(column=2, row=3, sticky="EW")

add = Button(text="Add", width=37, command=save)
add.grid(column=1, row=4, columnspan=2, sticky="EW")

# Entries
website_entry = Entry(width=43)
website_entry.grid(column=1, row=1, columnspan=2, sticky="EW")
website_entry.focus()

email_entry = Entry(width=43)
email_entry.grid(column=1, row=2, columnspan=2, sticky="EW")
email_entry.insert(0, "franco@hotmail.com")

password_entry = Entry(width=25)
password_entry.grid(column=1, row=3, sticky="EW")

window.mainloop()
