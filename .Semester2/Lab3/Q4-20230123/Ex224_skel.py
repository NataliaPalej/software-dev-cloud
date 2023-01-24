from tkinter import *
from Ex224MyClasses import *

window = Tk()
window.geometry("300x360")
window.title("Welcome")


# ------------end of class definition------------------
def display():
    value1 = t1.getTitle()
    value2 = t1.getAuthor()
    value3 = t1.getFormat()
    value4 = t1.getPlayingTime()
    value5 = t1.getIsbn()
    entry2.delete(0, END)  # delete old value
    entry2.insert(END, value1)
    entry3.delete(0, END)  # delete old value
    entry3.insert(END, value2)
    entry4.delete(0, END)  # delete old value
    entry4.insert(END, value3)
    entry5.delete(0, END)  # delete old value
    entry5.insert(END, value4)
    entry6.delete(0, END)  # delete old value
    entry6.insert(END, value5)


def changeAuthorEvent():
    newAuthor = entry3a.get()
    t1.setAuthor(newAuthor)
    display()


def resetFormatEvent():
    newFormat = entry3b.get()
    t1.setFormat(newFormat)
    display()


def resetPlayTimeEvent():
    newTime = int(entry4b.get())
    t1.setPlayTime(newTime)
    display()


def addToPlayTimeEvent():
    amount = int(entry5b.get())
    t1.addToPlayTime(amount)
    display()


t1 = AudioBook("Python 2", "T.Andrews", "MP3", 195, "SB0234523")

label1 = Label(window, text="AudioBook Details", fg="black", bg="mediumpurple1", font=("arial", 16, "bold"))  #
label1.place(x=50, y=30)  # place on screen

label2 = Label(window, text="Title", fg="black", width=8, font=("arial", 10, "bold"))  #
label2.place(x=60, y=80)

entry2 = Entry(window)
entry2.insert(END, '1')
entry2.place(x=120, y=80)

label3 = Label(window, text="Author", fg="black", width=12, font=("arial", 10, "bold"))  #
label3.place(x=40, y=110)

entry3 = Entry(window)
entry3.insert(END, '1')
entry3.place(x=120, y=110)

label4 = Label(window, text="Format", fg="black", width=8, font=("arial", 10, "bold"))  #
label4.place(x=50, y=140)

entry4 = Entry(window)
entry4.insert(END, '1')
entry4.place(x=120, y=140)

label5 = Label(window, text="Playing Time", fg="black", width=12, font=("arial", 10, "bold"))  #
label5.place(x=20, y=170)

entry5 = Entry(window)
entry5.insert(END, '1')
entry5.place(x=120, y=170)

label6 = Label(window, text="ISBN", fg="black", width=8, font=("arial", 10, "bold"))  #
label6.place(x=60, y=200)

entry6 = Entry(window)
entry6.insert(END, '')
entry6.place(x=120, y=200)

# -------------------------------
button1 = Button(window, text="changeAuthor", fg="black", bg="palevioletred1", width=13, font=("arial", 10, "bold"), command=changeAuthorEvent)
button1.place(x=2, y=230)

entry3a = Entry(window)
entry3a.insert(END, 'L.Williams')
entry3a.place(x=120, y=230)

# button2= Button(window, text="Exit", fg="black", font=("arial", 10, "bold"), command=exitEvent)
# button2.place(x=120, y=230)

button3 = Button(window, text="resetFormat", fg="black", bg="palevioletred1", width=13, font=("arial", 10, "bold"), command=resetFormatEvent)
button3.place(x=2, y=260)

entry3b = Entry(window)
entry3b.insert(END, 'MP4')
entry3b.place(x=120, y=260)

button4 = Button(window, text="resetPlayTime", fg="black", bg="palevioletred1", width=13, font=("arial", 10, "bold"), command=resetPlayTimeEvent)
button4.place(x=2, y=290)

entry4b = Entry(window)
entry4b.insert(END, '230')
entry4b.place(x=120, y=290)

button5 = Button(window, text="addToPlayTime", fg="black", bg="palevioletred1", width=13, font=("arial", 10, "bold"), command=addToPlayTimeEvent)
button5.place(x=2, y=320)

entry5b = Entry(window)
entry5b.insert(END, '20')
entry5b.place(x=120, y=320)

display()

mainloop()
