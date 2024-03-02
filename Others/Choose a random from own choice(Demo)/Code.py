from tkinter import *
from random import *

App = Tk()



App.title("Demo App")


inp = Entry(App)
inp.pack()

def display():
    INP = (inp.get().split(','))
    msg = Label(App, text=choice(INP))
    msg.pack()

B1 = Button(App, text='Pick' , command=display)
B1.pack()

App.mainloop()
