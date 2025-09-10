from tkinter import *
import random

obj = Tk()
obj.geometry("600x600+400+200")
obj.title("Password Generator")

num = list('0123456789')
upper = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
lower = list('abcdefghijklmnopqrstuvwxyz')
specialchar = list('`~!@#$%^&*()_+-=[]{}|/;:,<.>?')
allchar = upper + lower + num + specialchar

Label(text='Length:').place(x=100, y=20)

E = Entry(width=10)
E.place(x=160, y=20)

T = Text(width=65, height=25)
T.place(x=30, y=120)

def call(password):
    T.delete('1.0', END)
    T.insert(END, password)

def simple():
    try:
        n = int(E.get())
    except ValueError:
        call("Please enter a valid number")
        return

    password = ''.join(random.choice(upper + lower + num) for _ in range(n))
    call(password)

def complx():
    try:
        n = int(E.get())
    except ValueError:
        call(" Please enter a valid number")
        return

    password = ''.join(random.choice(allchar) for _ in range(n))
    call(password)


B1 = Button(text="Generate Simple Password", command=simple)
B1.place(x=100, y=70)

B2 = Button(text="Generate Complex Password", command=complx)
B2.place(x=300, y=70)

obj.mainloop()



