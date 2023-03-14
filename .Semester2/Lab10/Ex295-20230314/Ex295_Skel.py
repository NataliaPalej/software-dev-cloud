from tkinter import messagebox
from tkinter import *
from Ex295_MyClasses import *

window = Tk()
window.geometry("300x300")
window.title("Welcome")


def display():
    # read Name from Account
    value1 = a1.getName()
    # read Balance from Account
    value2 = a1.getBalance()
    entry2.delete(0, END)
    entry2.insert(END, value1)
    entry3.delete(0, END)
    entry3.insert(END, value2)


def depositEvent():
    amt = int(entry4.get())
    a1.deposit(amt)
    display()


def withdrawEvent():
    amt = int(entry5.get())
    balance = a1.getBalance()
    if balance > amt:
        a1.withdraw(amt)
        display()
        result = True
    else:
        message = "Insufficient Funds!"
        entry6.delete(0, END)
        entry6.insert(END, message)

        messagebox.showinfo("Error", "Insufficient Funds! You have €{0} but trying to "
                                     "withdraw €{1}".format(balance, amt))
        result = False
    return result


# create an Account object
a1 = Account("J.Smith", 500)

label1 = Label(window, text="Account Details", fg="black", bg="tomato", font=("arial", 16, "bold"))  #
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

button4 = Button(window, text="Deposit", fg="black", bg="plum1", font=("arial", 10, "bold"), command=depositEvent)
button4.place(x=40, y=140)
entry4 = Entry(window)
entry4.insert(END, '30')
entry4.place(x=120, y=140)

button5 = Button(window, text="Withdraw", fg="black", bg="plum1", font=("arial", 10, "bold"), command=withdrawEvent)
button5.place(x=40, y=180)
entry5 = Entry(window)
entry5.insert(END, '20')
entry5.place(x=120, y=180)

label4 = Label(window, text="Message", fg="black", width=8, font=("arial", 10, "bold"))
label4.place(x=40, y=240)
entry6 = Entry(window)
entry6.insert(END, 0)
entry6.place(x=120, y=240)

display()

mainloop()
