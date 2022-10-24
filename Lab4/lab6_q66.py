from tkinter import *
from tkinter import messagebox

window = Tk()
window.geometry("300x300")
window.title("Welcome")


class Stepper:
    def __init__(self):
        self.amt = 1
        self.__val = 1

    def get_value(self):
        return self.__val

    def step_up(self, amt):
        print("Previous value: {0}".format(self.amt))
        self.amt += amt
        print("New value {0}".format(self.amt))
        self.__val += amt

    def step_down(self, amt):
        if self.__val < 0 or self.__val < amt:
            messagebox.showinfo("Error", "Cannot go below 0")
        else:
            print("Previous value: {0}".format(self.amt))
            self.amt -= amt
            print("New value {0}".format(self.amt))
            self.__val -= amt

    def reset(self, amt):
        self.amt = amt
        print("Retested to value {0}".format(amt))
        self.__val = 1


# ------------end of class definition------------------

def display():
    value1 = a1.get_value()
    value2 = 0
    entry2.delete(0, END)  # delete old value
    entry2.insert(END, value1)


def deposit_event():
    amt = int(entry4.get())
    a1.step_up(amt)
    display()


def reset_event():
    amt = int(entry3.get())
    a1.reset(amt)
    display()


def withdraw_event():
    amt = int(entry5.get())
    a1.step_down(amt)
    display()


a1 = Stepper()


label1 = Label(window, text="Stepper Details", fg="black", bg="pink", font=("arial", 16, "bold"))   #
label1.place(x=70, y=30)                            # place on screen

button4 = Button(window, text="Reset", fg="black", font=("arial", 10, "bold"), command=reset_event)
button4.place(x=40, y=110)

entry2 = Entry(window)
entry2.insert(END, '1')
entry2.place(x=120, y=80)

label3 = Label(window, text="Value", fg="black", width=8, font=("arial", 10, "bold"))   #
label3.place(x=10, y=80)

entry3 = Entry(window)
entry3.insert(END, '1')
entry3.place(x=120, y=110)


button4 = Button(window, text="Step Up", fg="black", bg="pink", font=("arial", 10, "bold"), command=deposit_event)
button4.place(x=40, y=140)

entry4 = Entry(window)
entry4.insert(END, '30')
entry4.place(x=120, y=140)

button5 = Button(window, text="Step Down", fg="black", bg="pink", font=("arial", 10, "bold"), command=withdraw_event)
button5.place(x=40, y=180)

entry5 = Entry(window)
entry5.insert(END, '20')
entry5.place(x=120, y=180)


display()

mainloop()
