from tkinter import *
window = Tk()
window.geometry("300x300")
window.title("Welcome")


class Stepper:
    def __init__(self, val):
        self.__val = val

    def get_value(self):
        return self.__val

    def step_up(self, amt):
        self.__val += amt

    def decrement(self, amt):
        if self.__val < amt:
            self.__val -= amt
            return False
        else:
            return True

    def reset(self, amt):
        self.__val = amt



# ------------end of class definition------------------

def display():
    value1 = a1.get_value()
    value2 = 0
    entry2.delete(0, END)  # delete old value
    entry2.insert(END, value1)


def deposit_event():
    entry5.delete(0, END)  # delete old value
    amt = int(entry4.get())
    a1.step_up(amt)
    display()

def reset_event():
    entry5.delete(0, END)  # delete old value
    amt = int(entry3.get())
    a1.reset(amt)
    display()

def decrement_event():
    amt = int(entry4.get())
    result = a1.decrement(amt)
    display()
    if (result == False):
        entry5.delete(0, END)  # delete old value
        entry5.insert(END, 'Already 0')
    else:
        entry5.delete(0, END)  # delete old value
        entry5.insert(END, '')



a1=Stepper(2)


label1 = Label(window, text="Stepper Details", fg="blue",bg="yellow", font=("arial", 16, "bold"))   #
label1.place(x=90, y=30)                            # place on screen


button4= Button(window, text="Reset", fg="black", font=("arial", 10, "bold"), command=reset_event)
button4.place(x=40, y=110)


entry2 = Entry(window)
entry2.insert(END, '1')
entry2.place(x=120, y=80)

label3 = Label(window, text="Value", fg="blue", width=8, font=("arial", 10, "bold"))   #
label3.place(x=10, y=80)

entry3 = Entry(window)
entry3.insert(END, '1')
entry3.place(x=120, y=110)



button4= Button(window, text="stepUp", fg="black", font=("arial", 10, "bold"), command=deposit_event)
button4.place(x=40, y=140)

entry4 = Entry(window)
entry4.insert(END, '2')
entry4.place(x=120, y=140)

button5= Button(window, text="Decrement", fg="black", font=("arial", 10, "bold"), command=decrement_event)
button5.place(x=39, y=180)

entry5 = Entry(window)
entry5.insert(END, '')
entry5.place(x=120, y=180)


display()

mainloop()
