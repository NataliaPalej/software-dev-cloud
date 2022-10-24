from tkinter import *

window = Tk()
window.geometry("300x300")
window.title("Welcome")


class Account:
    def __init__(self, name, balance):
        self.__name = name
        self.__balance = balance

    def get_balance(self):
        return self.__balance

    def set_balance(self, balance):
        self.__balance = balance

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def deposit(self, amt):
        self.__balance += amt
        print("You deposited: €{0}\n\tYour new balance is: €{1}".format(amt, self.__balance))

    def withdraw(self, amt):
        if amt <= self.__balance:
            self.__balance = self.__balance - amt
            print("You withdrawn €{0}\n\tYour balance is: €{1}".format(amt, self.__balance))
        else:
            print("NOT ENOUGH FUNDS\nYou tried to withdraw "
                  "€{0}\n\tYour current balance is: €{1}".format(amt, self.__balance))

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


def withdraw_event():
    amt = int(entry5.get())
    a1.withdraw(amt)
    display()


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

button4 = Button(window, text="Deposit", fg="black", font=("arial", 10, "bold"), command=deposit_event)
button4.place(x=40, y=140)

entry4 = Entry(window)
entry4.insert(END, '30')
entry4.place(x=120, y=140)

button5 = Button(window, text="Withdraw", fg="black", font=("arial", 10, "bold"), command=withdraw_event)
button5.place(x=40, y=180)

entry5 = Entry(window)
entry5.insert(END, '20')
entry5.place(x=120, y=180)

display()
mainloop()
