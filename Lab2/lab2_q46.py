from tkinter import *
from tkinter import messagebox
window = Tk()
window.geometry("300x300")
window.title("Welcome")

invoice_ID = 0                                  # global variable to store invoice number


def get_price():
    global invoice_ID
    invoice_ID = invoice_ID + 1

    nights = int(entry2.get())
    guests = int(guestVar.get())
    cots = int(cotsVar.get())
    price = (50 * nights) + (10 * cots)
    if var_cb2.get() > 0:                         # dinner included
        price = price + (guests * 30 * nights)
        print("Dinner included")
    if var_cb1.get() > 0:                         # breakfast included
        price = price + (guests * 10 * nights)
        print("Breakfast included")
    entry3.delete(0, END)
    entry3.insert(END, '$')
    entry3.insert(END, price)
    print("Guests: {0}\nNights: {1}\nCots: {2}\n\tTotal: ${3}\nInvoice number: {4}".format(guestVar.get(), entry2.get(),
                                                                      cotsVar.get(), price, invoice_ID))
    print()


def receipt_message():
    global invoice_ID               # incrementing invoice number
    invoice_ID = invoice_ID + 1

    total = entry3.get()            # get all parameters for receipt
    nights = entry2.get()
    guests = guestVar.get()
    cots = cotsVar.get()
    breakfast = var_cb1.get()
    dinner = var_cb2.get()
    if breakfast > 0:
        breakfast = "Yes"           # display breakfast included
    else:
        breakfast = "No"
    if dinner > 0:
        dinner = "Yes"              # display dinner included
    else:
        dinner = "No"
    messagebox.showinfo("Receipt", "{0} Invoice: {1}\nNights: {2}\nGuests: {3}\nCots: {4}\nBreakfast: {5}"
                                   "\nDinner: {6}".format(invoice_ID, total, nights, guests, cots, breakfast, dinner))


frame = Frame(window, width=200, height=200)
frame.place(x=10, y=80)
label1 = Label(window, text="Hotel Application", fg="black", bg="pink", font=("arial", 16, "bold"))
label1.place(x=70, y=30)

label2 = Label(frame, text="Nights", fg="Black", width=15, font=("arial", 10, "bold"))
label2.grid(row=0, column=0, sticky=W+E)

entry2 = Entry(frame)
entry2.insert(END, '1')
entry2.grid(row=0, column=1, sticky=W+E)

label3 = Label(frame, text="Guests", fg="Black", width=15, font=("arial", 10, "bold"))
label3.grid(row=1, column=0, sticky=W+E)

label4 = Label(frame, text="Cots", fg="Black", width=15, font=("arial", 10, "bold"))
label4.grid(row=2, column=0, sticky=W+E)

list1 = ['1', '2', '3', '4']
guestVar = StringVar()
combo1 = OptionMenu(frame, guestVar, *list1)
guestVar.set("1")
combo1.grid(row=1, column=1, sticky=W+E)

list2 = ['0', '1', '2', '3', '4']
cotsVar = StringVar()
combo1 = OptionMenu(frame, cotsVar, *list2)
cotsVar.set("1")
combo1.grid(row=2, column=1, sticky=W+E)

var_cb1 = IntVar()
cb1 = Checkbutton(frame, text="Breakfast", variable=var_cb1)
cb1.grid(row=3, column=0)
cb1.deselect()

var_cb2 = IntVar()
cb1 = Checkbutton(frame, text="Dinner", variable=var_cb2)
cb1.grid(row=3, column=1)
cb1.deselect()

button1 = Button(frame, text="Get Price", fg="black", font=("arial", 8, "bold"), command=get_price)
button1.grid(row=4, column=0, sticky=W+E)

button2 = Button(frame, text="Receipt", fg="black", font=("arial", 8, "bold"), command=receipt_message)
button2.grid(row=5, column=0, sticky=W+E)

entry3 = Entry(frame)
entry3.insert(END, 0)
entry3.grid(row=4, column=1, sticky=W+E)

mainloop()
