############################ GRID ################

from asyncore import close_all
from tkinter import *

window = Tk()

window.title("Abdul @ life.com", )
window.minsize(width=500, height=300)
my_label = Label(text="My Text", font=("Arial", 24, "bold"))
my_label.grid(column=0, row=0)

# my_label["text"] = "Text Area"
my_label.config(text="Text New")

# Button
def button_click():
    print("Am clicked")

button = Button(text="Button-1", command=button_click, fg="red", bg="black")
button.grid(column=1, row=1)

button_2 = Button(text="New Button")
button_2.grid(column=2,row=0)

input = Entry(width=10, bg="green")
print(input.get())
input.grid(column=3, row=2)

window.mainloop()