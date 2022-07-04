from tkinter import *

def convert():
    value["text"] = f"{round(float(input.get())*1.60934)}"

#window
window = Tk()
window.title("Miles to Kilometer Converter")
# window.minsize(width=500, height=500)
window.config(padx=20, pady=20)

#Input
input = Entry(width=7)
input.grid(column=1, row=0)

#Button
button = Button(text="Calculate", command=convert)
button.grid(column=1, row=2)

#Labels
is_equal_to = Label(text="Is equal to")
is_equal_to.grid(column=0, row=1)

miles = Label(text="Miles")
miles.grid(column=3, row=0)

value = Label(text="0")
value.grid(column=1, row=1)

km = Label(text="Km")
km.grid(column=2, row=1)







window.mainloop()