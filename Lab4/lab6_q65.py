from tkinter import *
import random

window = Tk()
window.geometry("300x300")
window.title("Welcome")


class Dice:
    def __init__(self):             # set initial value to 1
        self.__val = 1

    def get_value(self):            # get dice value
        return self.__val

    def set_value(self, val):       # set new dice value
        self.__val = val

    def roll(self):                 # roll random number
        self.__val = random.randint(1, 6)
        print("You rolled {0}".format(self.__val))


# ------------end of class definition------------------


def display():
    value1 = d1.get_value()
    entry2.delete(0, END)  # delete old value
    entry2.insert(END, value1)


def roll_event():
    d1.roll()
    display()


def reset_event():
    d1.set_value(1)
    display()


d1 = Dice()

label1 = Label(window, text="Dice ", fg="black", bg="pink", font=("arial", 16, "bold"))  #
label1.place(x=90, y=30)  # place on screen

label2 = Label(window, text="Value", fg="black", width=8, font=("arial", 10, "bold"))  #
label2.place(x=10, y=80)

entry2 = Entry(window)
entry2.insert(END, '1')
entry2.place(x=120, y=80)

# -------------------------------
button1 = Button(window, text="Roll Dice", fg="black", bg="pink", font=("arial", 10, "bold"), command=roll_event)
button1.place(x=40, y=120)

button2 = Button(window, text="Reset", fg="black", bg="pink", font=("arial", 10, "bold"), command=reset_event)
button2.place(x=120, y=120)

display()

mainloop()
