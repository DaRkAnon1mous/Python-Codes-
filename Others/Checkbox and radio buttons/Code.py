

check = IntVar()
chk1 = Checkbutton(App, text='Checkbox1',variable=check,onvalue=1,offvalue=2)
chk1.deselect()
chk1.grid()

rb1 = Radiobutton(App, text="Radiobutton")
rb1.grid()

