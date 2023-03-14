from tkinter import *
from tkinter import messagebox

window = Tk()
window.geometry("300x300")
window.title("Welcome")


def reset():
    daysVar.set("1")
    seatsVar.set("5")
    cb1.deselect()
    cb2.deselect()
    entry3.delete(0, END)
    entry3.insert(END, " ")


def info():
    messagebox.showinfo(title="Car Hire", message="From €50/day - 5 seater\nSat Nav optional - €10/day\n"
                                                          "Insurance optional - €15/day")


menu1 = Menu(window)
window.config(menu=menu1)

submenu = Menu(menu1)
menu1.add_cascade(label="Admin", menu=submenu)
submenu.add_cascade(label="Clear", command=reset)
submenu.add_cascade(label="Help", command=info)


def getQuote():
    days = int(daysVar.get())
    seats = int(seatsVar.get())
    quote = 50 * days
    if seats == 7:
        quote = 70 * days
    elif seats == 9:
        quote = 80 * days

    if var_cb1.get() > 0:
        quote = quote + (10 * days)

    if var_cb2.get() > 0:
        quote = quote + (15 * days)
    entry3.delete(0, END)
    entry3.insert(END, '€')
    entry3.insert(END, quote)


frame = Frame(window, width=200, height=200)
frame.place(x=10, y=80)
label1 = Label(window, text="Car Hire Application", fg="black", bg="tomato", font=("arial", 16, "bold"))
label1.place(x=50, y=30)  # place on screen

label2 = Label(frame, text="No of Days", fg="black", width=15, font=("arial", 10, "bold"))  #
label2.grid(row=0, column=0, sticky=W + E)

list0 = ['1', '2', '3', '4', '5', '6', '7']
daysVar = StringVar()
combo0 = OptionMenu(frame, daysVar, *list0)
daysVar.set("1")
combo0.grid(row=0, column=1, sticky=W + E)

label3 = Label(frame, text="Seats", fg="black", width=15, font=("arial", 10, "bold"))  #
label3.grid(row=1, column=0, sticky=W + E)

list1 = ['5', '7', '9']
seatsVar = StringVar()
combo1 = OptionMenu(frame, seatsVar, *list1)
seatsVar.set("5")
combo1.grid(row=1, column=1, sticky=W + E)

var_cb1 = IntVar()  # 0 unchecked, 1 checked
cb1 = Checkbutton(frame, text="Sat Nav   ", variable=var_cb1)
cb1.grid(row=2, column=0, columnspan=2)
cb1.deselect()

var_cb2 = IntVar()  # 0 unchecked, 1 checked
cb2 = Checkbutton(frame, text="Insurance", variable=var_cb2)
cb2.grid(row=3, column=0, columnspan=2)
cb2.deselect()

button1 = Button(frame, text="GetQuote", fg="black", font=("arial", 8, "bold"), command=getQuote)
button1.grid(row=4, column=0, sticky=W + E)

entry3 = Entry(frame)
entry3.insert(END, '0')
entry3.grid(row=4, column=1, sticky=W + E)

mainloop()
