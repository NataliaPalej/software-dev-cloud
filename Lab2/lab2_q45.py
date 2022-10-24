from tkinter import *
window = Tk()
window.geometry("300x300")
window.title("Welcome")

var_cb1 = IntVar()  # 0 unchecked, 1 checked
cb1 = Checkbutton(window, text = "Negative", variable=var_cb1)
cb1.place(x=90, y=170)
#cb1.grid(row=17, column=3, columnspan=2)  # instead of place

def stepup():
    value1 = int(entry2.get())
    value2 = int(stepUpVar.get())
    result = value1 + value2
    if result < 0:
        cb1.select()
    elif result >= 0:
        cb1.deselect()
    print("status={}".format(result))
    entry2.delete(0, END)
    entry2.insert(END, result)

def stepdown():
    value1 = int(entry2.get())
    value2 = int(stepDownVar.get())
    result = value1 - value2
    if result < 0:
        cb1.select()
    elif result >= 0:
        cb1.deselect()
    print("status={}".format(result))
    entry2.delete(0, END)
    entry2.insert(END, result)


frame = Frame(window, width=200, height=200)
frame.place(x=50,y=80)
label1 = Label(window, text="Grid example", fg="black", bg="pink", font=("arial", 16, "bold"))
label1.place(x=90, y=30)                            # place on screen

label2 = Label(frame, text="Value", fg="black", font=("arial", 10, "bold"))   #
label2.grid(row=0, column=0, sticky=W+E)

entry2 = Entry(frame)
entry2.insert(END, '1')
entry2.grid(row=0, column=1, sticky=W+E)

#entry3 = Entry(frame)
#entry3.insert(END, '1')
#entry3.grid(row=0, column=1, sticky=W+E)

button1 = Button(frame, text="StepUp", fg="black", font=("arial", 10, "bold"), command=stepup)
button1.grid(row=1, column=0, sticky=W+E)

button2 = Button(frame, text="StepDown", fg="black", font=("arial", 10, "bold"), command=stepdown)
button2.grid(row=2, column=0, sticky=W+E)




list1 = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
stepUpVar = StringVar()
combo1 = OptionMenu(frame, stepUpVar, *list1)
stepUpVar.set("1")
combo1.grid(row=1, column=1, sticky=W+E)

stepDownVar = StringVar()
combo2 = OptionMenu(frame, stepDownVar, *list1)
stepDownVar.set("1")
combo2.grid(row=2, column=1, sticky=W+E)


mainloop()
