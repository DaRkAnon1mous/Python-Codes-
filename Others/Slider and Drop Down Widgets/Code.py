Sld = Scale(App, from_=0,to=100, orient=HORIZONTAL)
Sld.grid()

menu_ch = StringVar()
options = ['Red','White','Green','Yellow']
menu = OptionMenu(App,menu_ch,*options)
menu_ch.set('White')
menu.grid()
