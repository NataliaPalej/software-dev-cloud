from tkinter import *
from tkinter import messagebox
import random

window = Tk()
window.geometry("300x300")
window.title("Car Loan App")


def getQuote():
    type = str(typeVar.get())
    days = int(daysVar.get())
    passengers = int(passengersVar.get())

    basePrice = 50                      # car type
    if type == 'Medium':
        basePrice = 70
    if type == 'Large':
        basePrice = 90
    quote = basePrice * days
    if var_cb1.get() > 0:
        quote = quote + (days * 10)
    ins = var_cb1.get()
    if ins > 0:                         # insurance - yes/no
        ins = "Yes €10/day"
    elif ins <= 0:
        ins = "No"
    if passengers > 5:                  # passengers extra 120 if more than 5
        quote = quote + 120
    if var_cb2.get() > 0:
        quote = quote + (days * 5)
    sat_nav = var_cb2.get()
    if sat_nav > 0:                     # sat nav - yes/no
        sat_nav = "Yes €5/day"
    else:
        sat_nav = "No"
    entry3.delete(0, END)
    entry3.insert(END, '€')
    entry3.insert(END, str(quote))
    print("Quote: €{0}\nBase Price: €{1}\nCar Type: {2}\nInsurance: {3}\t\tSat Nav: {4}\nNumber of days: {5}"
          "\nPassengers: {6}\n*Extra charge of €120 for more than 5 "
          "passengers*\n".format(quote, basePrice, type, ins, sat_nav, days, passengers))


def reset():
    entry3.delete(0, END)
    entry3.insert(END, 0)
    daysVar.set("1")
    passengersVar.set("0")
    typeVar.set("Medium")
    cb1.deselect()
    cb2.deselect()


def my_exit():
    exit()


def contact():
    def close2():
        window2.destroy()

    window2 = Tk()
    window2.geometry("300x120")
    window2.title("Contact")
    contact_label = Label(window2, text="Phone number\n089 478 7485", fg="black", bg="pink", font=("arial", 14))
    contact_label.place(x=80, y=20)
    button_exit = Button(window2, text="Exit", fg="black", font=("arial", 10), command=close2)
    button_exit.place(x=130, y=80)


def receipt():
    invoice = random.randint(0, 9999)
    quote = entry3.get()
    insurance = var_cb1.get()
    sat_nav = var_cb2.get()
    type = str(typeVar.get())
    days = int(daysVar.get())
    passengers = int(passengersVar.get())

    if insurance > 0:
        insurance = "Yes"
    else:
        insurance = "No"
    if sat_nav > 0:
        sat_nav = "Yes"
    else:
        sat_nav = "No"
    messagebox.showinfo("Receipt", "Total: {0}\nDays: {1}\nInsurance: {2}\nSat Nav: {3}\nPassengers: {4}"
                                   "\nCar Type: {5}\nInvoice: {6}".format(quote, days, insurance, sat_nav, passengers, type, invoice))


menu1 = Menu(window)
window.config(menu=menu1)

sub_menu = Menu(menu1)
menu1.add_cascade(label="Options", menu=sub_menu)
sub_menu.add_command(label="Reset", command=reset)
sub_menu.add_command(label="Exit", command=my_exit)

sub_menu2 = Menu(menu1)
menu1.add_cascade(label="Contact", menu=sub_menu2)
sub_menu2.add_command(label="Help", command=contact)

frame = Frame(window, width=200, height=200)
frame.place(x=10, y=80)
label1 = Label(window, text="Car Loan Application", fg="black", bg="pink", font=("arial", 16, "bold"))
label1.place(x=40, y=30)  # place on screen

label2 = Label(frame, text="Car Type", fg="black", width=15, font=("arial", 10, "bold"))  #
label2.grid(row=0, column=0, sticky=W + E)

list0 = ['Small', 'Medium', 'Large']
typeVar = StringVar()
combo0 = OptionMenu(frame, typeVar, *list0)
typeVar.set("Medium")
combo0.grid(row=0, column=1, sticky=W + E)

label3 = Label(frame, text="Days", fg="black", width=15, font=("arial", 10, "bold"))  #
label3.grid(row=1, column=0, sticky=W + E)

label3 = Label(frame, text="Passengers", fg="black", width=15, font=("arial", 10, "bold"))  #
label3.grid(row=2, column=0, sticky=W + E)

list1 = ['1', '2', '3', '4', '5', '6']                      # number of rental days
daysVar = StringVar()
combo1 = OptionMenu(frame, daysVar, *list1)
daysVar.set("1")
combo1.grid(row=1, column=1, sticky=W + E)

# --------------------------------

list2 = ['0', '1', '2', '3', '4', '5', '6', '7']            # passengers amount
passengersVar = StringVar()
combo2 = OptionMenu(frame, passengersVar, *list2)
passengersVar.set('0')
combo2.grid(row=2, column=1, sticky=W+E)

# ------------------------------------

var_cb1 = IntVar()  # 0 unchecked, 1 checked                        # insurance check box
cb1 = Checkbutton(frame, text="Insurance", variable=var_cb1)
cb1.grid(row=3, column=0, columnspan=1)
cb1.deselect()

# --------------------------------

var_cb2 = IntVar()  # 0 unchecked, 1 checked                        # sat nav check box
cb2 = Checkbutton(frame, text="SatNav", variable=var_cb2)
cb2.grid(row=3, column=1, columnspan=1)
cb2.deselect()

# ------------------------------------

button1 = Button(frame, text="GetPrice", fg="black", font=("arial", 8, "bold"), command=getQuote)
button1.grid(row=5, column=0, sticky=W + E)

button2 = Button(frame, text="Receipt", fg="black", font=("arial", 8, "bold"), command=receipt)
button2.grid(row=6, column=0, sticky=W+E)

entry3 = Entry(frame)
entry3.insert(END, '0')
entry3.grid(row=5, column=1, sticky=W + E)

mainloop()
