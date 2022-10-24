from tkinter import *
window = Tk()
window.geometry("300x300")
window.title("Welcome")

def add():
    value1 = int(entry1.get())
    value2 = int(entry2.get())
    result = value1 + value2
    entry3.delete(0, END)
    entry3.insert(END, result)

def sub():
    value1 = int(entry1.get())
    value2 = int(entry2.get())
    result = value1 - value2
    entry4.delete(0, END)
    entry4.insert(END, result)

def reset():
    entry1.delete(0, END)
    entry1.insert(END, 0)
    entry2.delete(0, END)
    entry2.insert(END, 0)
    entry3.delete(0, END)
    entry3.insert(END, 0)
    entry4.delete(0, END)
    entry4.insert(END, 0)

label1 = Label(window, text="Calculator", fg="black",bg="pink", font=("arial", 16, "bold"))   #
label1.place(x=90, y=30)

label2 = Label(window, text="Value 1", fg="black", width=10, font=("arial", 12, "bold"))   #
label2.place(x=10, y=80)

label2 = Label(window, text="Value 2", fg="black", width=10, font=("arial", 12, "bold"))   #
label2.place(x=10, y=114)

entry1 = Entry(window)
entry1.insert(END, "0")
entry1.place(x=100, y=80)

entry2 = Entry(window)
entry2.insert(END, '0')
entry2.place(x=100, y=115)

entry3 = Entry(window)
entry3.insert(END, '0')
entry3.place(x=100, y=155)

entry4 = Entry(window)
entry4.insert(END, '0')
entry4.place(x=100, y=195)

button1 = Button(window, text="Add", width="7", fg="black", bg="pink", font=("arial", 10, "bold"), command=add)
button1.place(x=30, y=150)

button2 = Button(window, text="Subtract", fg="black", bg="pink", font=("arial", 10, "bold"), command=sub)
button2.place(x=30, y=190)

button3 = Button(window, text="Reset", fg="white", bg="black", font=("arial", 9, "bold"), command=reset)
button3.place(x=10, y=260)

mainloop()