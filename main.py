from tkinter import *


def action():
    if label['text'] == "Enter the value in Miles":
        miles = entry.get()
        km = str(round(1.609344 * float(miles), 2))
        label3.config(text=km)
    if label['text'] == "Enter the value in KM":
        km = entry.get()
        miles = str(round(float(km)/1.609344, 2))
        label3.config(text=miles)


def action_inverse():
    action()
    if label['text'] == "Enter the value in Miles":
        label.config(text="Enter the value in KM")
        label2.config(text="The value in Miles")
    else:
        label.config(text="Enter the value in Miles")
        label2.config(text="The value in Miles")



window = Tk()
window.title("Miles to KM Converter")
window.minsize(width=150, height=175)

label = Label(text="Enter the value in Miles", font=("Arial", 20, "bold"))
label.grid(column=0, row=0)

entry = Entry(width=30)
entry.insert(END, string="0")
entry.grid(column=0, row=1)

label2 = Label(text="The value in KM", font=("Arial", 20, "bold"))
label2.grid(column=0, row=2)

label3 = Label(text="0", font=("Arial", 20, "bold"))
label3.grid(column=0, row=3)

button = Button(text="Convert", command=action)
button.grid(column=0, row=4)

button2 = Button(text="Swap", command=action_inverse)
button2.grid(column=0, row=5)

window.mainloop()
