from tkinter import *

window = Tk()
window.geometry("300x300")
window.title("Welcome")


class Pair:
    def __init__(self, val1, val2):  # public method that sets two values
        self.__value = val1  # initializing val1 and val2, both private
        self.__value2 = val2

    def set_value(self, val1):
        self.__value = val1

    def get_value(self):
        return self.__value

    def set_value2(self, val2):
        self.__value2 = val2

    def get_value2(self):
        return self.__value2

    def incr_value1(self):
        self.__value += 1
        print("Val1  incremented by one: {0}".format(self.__value))

    def incr_value2(self):
        self.__value2 += 1
        print("Val2 incremented by one: {0}".format(self.__value2))

    def add(self):  # adding method
        return self.__value + self.__value2

    def multiply(self):  # multiply method
        return self.__value * self.__value2


# ------------ end of class definition------------------


def display():
    value1 = p1.get_value()
    value2 = p1.get_value2()
    entry2.delete(0, END)  # delete old value
    entry2.insert(END, value1)
    entry3.delete(0, END)  # delete old value
    entry3.insert(END, value2)


def incr_v1_event():
    p1.incr_value1()
    display()


def incr_v2_event():
    p1.incr_value2()
    display()


def add_event():
    result = p1.add()
    display()
    entry4.delete(0, END)  # delete old value
    entry4.insert(END, result)
    print("{0} + {1} = {2}".format(p1.get_value(), p1.get_value2(), result))


def multiply_event():
    result = p1.multiply()
    display()
    entry5.delete(0, END)  # delete old value
    entry5.insert(END, result)
    print("{0} * {1} = {2}".format(p1.get_value(), p1.get_value2(), result))


p1 = Pair(3, 5)

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

button1 = Button(window, text="IncrementV1", fg="black", font=("arial", 12, "bold"), command=incr_v1_event)
button1.place(x=10, y=140)

button2 = Button(window, text="IncrementV2", fg="black", font=("arial", 12, "bold"), command=incr_v2_event)
button2.place(x=140, y=140)

button4 = Button(window, text="Add", fg="black", font=("arial", 10, "bold"), command=add_event)
button4.place(x=40, y=180)

entry4 = Entry(window)
entry4.insert(END, '')
entry4.place(x=120, y=180)

button5 = Button(window, text="Multiply", fg="black", font=("arial", 10, "bold"), command=multiply_event)
button5.place(x=40, y=220)

entry5 = Entry(window)
entry5.insert(END, '')
entry5.place(x=120, y=220)

display()

mainloop()
