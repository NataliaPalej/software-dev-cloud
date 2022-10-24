from tkinter import *

window = Tk()
window.geometry("300x300")
window.title("Welcome")


class Team:
    played = 0
    points = 0
    wins = 0

    def __init__(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    def get_played(self):
        return self.played

    def get_points(self):
        return self.points

    def get_wins(self):
        return self.wins

    def win(self):
        self.played += 1
        self.points += 3
        self.wins += 1
        print("You won!")

    def loss(self):
        self.played += 1
        print("You lost!")

    def draw(self):
        self.played += 1
        self.points += 1
        print("Draw!")


# ------------end of class definition------------------


def display():
    value1 = t1.get_name()
    value2 = t1.get_played()
    value3 = t1.get_points()
    entry2.delete(0, END)  # delete old value
    entry2.insert(END, value1)
    entry3.delete(0, END)  # delete old value
    entry3.insert(END, value2)
    entry4.delete(0, END)  # delete old value
    entry4.insert(END, value3)
    entry5.delete(0, END)  # delete old value


def win_event():
    t1.win()
    display()


def draw_event():
    t1.draw()
    display()


def loss_event():
    t1.loss()
    display()


def exit_event():
    quit()


def get_wins_event():
    result = t1.get_wins()
    entry5.delete(0, END)  # delete old value
    entry5.insert(END, result)
    print("You won {0} times".format(result))


t1 = Team("Chelsea")

label1 = Label(window, text="Team Details", fg="black", bg="pink", font=("arial", 16, "bold"))  #
label1.place(x=70, y=30)  # place on screen

label2 = Label(window, text="Name", fg="black", width=8, font=("arial", 10, "bold"))  #
label2.place(x=10, y=80)

entry2 = Entry(window)
entry2.insert(END, '1')
entry2.place(x=120, y=80)

label3 = Label(window, text="Played", fg="black", width=8, font=("arial", 10, "bold"))  #
label3.place(x=10, y=110)

entry3 = Entry(window)
entry3.insert(END, '1')
entry3.place(x=120, y=110)

label4 = Label(window, text="Points", fg="black", width=8, font=("arial", 10, "bold"))  #
label4.place(x=10, y=140)

entry4 = Entry(window)
entry4.insert(END, '1')
entry4.place(x=120, y=140)

# -------------------------------

button1 = Button(window, text="Win", fg="black", bg="pink", font=("arial", 10, "bold"), command=win_event)
button1.place(x=40, y=180)

button2 = Button(window, text="Draw", fg="black", bg="pink", font=("arial", 10, "bold"), command=draw_event)
button2.place(x=120, y=180)

button3 = Button(window, text="Loss", fg="black", bg="pink", font=("arial", 10, "bold"), command=loss_event)
button3.place(x=40, y=220)

button4 = Button(window, text="Exit", fg="black", bg="pink", font=("arial", 10, "bold"), command=exit_event)
button4.place(x=120, y=220)

button5 = Button(window, text="readWins", fg="black", font=("arial", 10, "bold"), command=get_wins_event)
button5.place(x=10, y=260)

entry5 = Entry(window)
entry5.insert(END, '')
entry5.place(x=120, y=260)

display()

mainloop()
