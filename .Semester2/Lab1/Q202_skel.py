from tkinter import *

window = Tk()
window.geometry("300x300")
window.title("Welcome")


class Treble:
    def __init__(self, val1, val2, val3):
        self.__val1 = val1
        self.__val2 = val2
        self.__val3 = val3

    def largest(self):
        if self.__val1 > self.__val2 and self.__val1 > self.__val3:
            return self.__val1
        elif self.__val2 > self.__val1 and self.__val2 > self.__val3:
            return self.__val2
        else:
            return self.__val3

    def reset_value2(self, amt):
        self.__val2 = amt

    def get_val1(self):
        return self.__val1

    def get_val2(self):
        return self.__val2

    def get_val3(self):
        return self.__val3

    def add(self):
        return self.__val1 + self.__val2 + self.__val3


# ------------end of class definition------------------


def display():
    value1 = c1.get_val1()
    value2 = c1.get_val2()
    value3 = c1.get_val3()
    entry2.delete(0, END)  # delete old value
    entry2.insert(END, value1)
    entry3.delete(0, END)  # delete old value
    entry3.insert(END, value2)
    entry4.delete(0, END)  # delete old value
    entry4.insert(END, value3)


def max_event():
    result = c1.largest()
    display()
    entry7.delete(0, END)  # delete old value
    entry7.insert(END, result)


def add_event():
    result = c1.add()
    display()
    entry6.delete(0, END)  # delete old value
    entry6.insert(END, result)


def reset_event():
    value = int(entry5.get())
    c1.reset_value2(value)
    display()


c1 = Treble(3, 5, 4)

label1 = Label(window, text="Welcome", fg="black", bg="pink", font=("arial", 16, "bold"))  #
label1.place(x=90, y=30)  # place on screen

label2 = Label(window, text="Value1", fg="black", width=8, font=("arial", 10, "bold"))  #
label2.place(x=10, y=80)

entry2 = Entry(window)
entry2.insert(END, '1')
entry2.place(x=120, y=80)

label3 = Label(window, text="Value2", fg="black", width=8, font=("arial", 10, "bold"))  #
label3.place(x=10, y=110)

entry3 = Entry(window)
entry3.insert(END, '1')
entry3.place(x=120, y=110)

label4 = Label(window, text="Value3", fg="black", width=8, font=("arial", 10, "bold"))  #
label4.place(x=10, y=140)

entry4 = Entry(window)
entry4.insert(END, '1')
entry4.place(x=120, y=140)

button0 = Button(window, text="resetV2", fg="black", bg="pink", width=7, font=("arial", 10,), command=reset_event)
button0.place(x=10, y=185)

entry5 = Entry(window)
entry5.insert(END, '1')
entry5.place(x=120, y=190)

button6 = Button(window, text="Add", fg="black", bg="pink", width=7, font=("arial", 10), command=add_event)
button6.place(x=10, y=225)

entry6 = Entry(window)
entry6.insert(END, '1')
entry6.place(x=120, y=230)

button7 = Button(window, text="Largest", fg="black", bg="pink", width=7, font=("arial", 10), command=max_event)
button7.place(x=10, y=265)

entry7 = Entry(window)
entry7.insert(END, '1')
entry7.place(x=120, y=270)
display()

mainloop()
