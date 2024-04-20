from tkinter import *
from random import *

App = Tk()



App.title("Demo App")
App.geometry('300x300')
App['background']='purple'


Display = Label(App,text='Generate a random Number', background='Blue',foreground='white')
Display.grid(row=0,column=3)

def show_msg():
    msg = Label(App, text=randint(1,100),background='Blue',foreground='white')
    msg.grid()

B = Button(App, text='Tap to generate a number' , command=show_msg,background='Blue',foreground='white')
B.grid(row=2, column=3,columnspan=2, padx=20)

inp = Entry(App,background='green',foreground='white')
inp.grid(row=8, column=3 , columnspan=2)

def display():
    INP = (inp.get().split(','))
    msg = Label(App, text=choice(INP),background='Blue',foreground='white')
    msg.grid()

    if QuitB['state'] == DISABLED:
        QuitB['state'] = NORMAL


B1 = Button(App, text='Pick' , command=display,background='Blue',foreground='white', relief='groove')
B1.grid()

QuitB = Button(App, text='Close',command=App.quit, state=DISABLED,background='Red',foreground='white')
QuitB.grid()

App.mainloop()
