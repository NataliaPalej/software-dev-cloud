from tkinter import *

window = Tk()
window.geometry("300x300")
window.title("ATM")


class InsuffFunds(Exception):
    pass


class MaxWithdraw (Exception):
    pass


class Account:
    def __init__(self, name, balance):
        self.__name = name
        self.__balance = balance

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if amount > 300:
            raise MaxWithdraw
        elif amount <= self.__balance:
            self.__balance -= amount
        else:
            raise InsuffFunds

    def get_name(self):
        return self.__name

    def get_balance(self):
        return self.__balance


# ------------end of class definition------------------


def display():
    value1 = a1.get_name()
    value2 = a1.get_balance()
    entry2.delete(0, END)  # delete old value
    entry2.insert(END, value1)
    entry3.delete(0, END)  # delete old value
    entry3.insert(END, value2)


def deposit_event():
    amt = int(entry4.get())
    a1.deposit(amt)
    display()
    entry6.delete(0, END)  # delete old value
    entry6.insert(END, 'Success')


def withdraw_event():
    try:
        amt = int(entry5.get())
        a1.withdraw(amt)
        display()
        entry6.delete(0, END)  # delete old value
        entry6.insert(END, 'Completed')
    except InsuffFunds:
        entry6.delete(0, END)  # delete old value
        entry6.insert(END, 'Insufficient Funds')
    except MaxWithdraw:
        entry6.delete(0, END)  # delete old value
        entry6.insert(END, 'Max amount exceeded')


a1 = Account("J.Smith", 500)

label1 = Label(window, text="Account Details", fg="black", bg="pink", font=("arial", 16, "bold"))  #
label1.place(x=70, y=30)  # place on screen

label2 = Label(window, text="Name", fg="black", width=8, font=("arial", 10, "bold"))  #
label2.place(x=10, y=80)

entry2 = Entry(window)
entry2.insert(END, '1')
entry2.place(x=120, y=80)

label3 = Label(window, text="Balance", fg="black", width=8, font=("arial", 10, "bold"))  #
label3.place(x=10, y=110)

entry3 = Entry(window)
entry3.insert(END, '1')
entry3.place(x=120, y=110)

button4 = Button(window, text="Deposit", fg="black", bg="pink", font=("arial", 10, "bold"), command=deposit_event)
button4.place(x=40, y=140)

entry4 = Entry(window)
entry4.insert(END, '30')
entry4.place(x=120, y=140)

button5 = Button(window, text="Withdraw", fg="black", bg="pink", font=("arial", 10, "bold"), command=withdraw_event)
button5.place(x=40, y=180)

entry5 = Entry(window)
entry5.insert(END, '20')
entry5.place(x=120, y=180)

label6 = Label(window, text="Message", fg="black", width=8, font=("arial", 10, "bold"))  #
label6.place(x=10, y=220)

entry6 = Entry(window)
entry6.insert(END, '')
entry6.place(x=120, y=220)

display()
mainloop()
