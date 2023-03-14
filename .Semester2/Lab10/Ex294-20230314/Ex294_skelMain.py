from Ex294_skelSub1 import *
from Ex294_sub2 import *
from tkinter import *

window = Tk()
window.geometry("300x300")
window.title("Welcome")

frame = Frame(window, width=200, height=200)
frame.place(x=10, y=80)
label1 = Label(window, text="Dialog example", fg="black", bg="tomato", font=("arial", 16, "bold"))
label1.place(x=60, y=30)  # place on screen

label2 = Label(frame, text="Options", fg="black", width=15, font=("arial", 10, "bold"))  #
label2.grid(row=0, column=0, sticky=W + E)

button1 = Button(frame, text="AddDialog", fg="black", bg="palegreen", font=("arial", 10, "bold"),
                 command=lambda: addDialog(window))
button1.grid(row=1, column=0, sticky=W + E)

button2 = Button(frame, text="SubDialog", fg="black", bg="orchid1", font=("arial", 10, "bold"),
                 command=lambda: subDialog(window))
button2.grid(row=2, column=0, sticky=W + E)

mainloop()
