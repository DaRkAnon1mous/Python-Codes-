from tkinter import *
from random import *

App = Tk()

App.title("Demo App")


Display = Label(App,text='Generate a random Number')
Display.pack()
App.geometry('300x300')

def show_msg():
    msg = Label(App, text=randint(1,100))
    msg.pack()

B = Button(App, text='Tap to generate a number' , command=show_msg)
B.pack()



App.mainloop()
