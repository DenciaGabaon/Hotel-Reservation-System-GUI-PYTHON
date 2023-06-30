from tkinter import *
from PIL import Image, ImageTk
from MENUFRAME import *

class MYCLASS:
    def HI(self):
        hotelinfo = Frame(menuWindow, bd=0, bg='white', width=830, height=475)
        hotelinfo.place(x=322, y=211)

        test = Label(hotelinfo, text="test hotel info frame", font=('tahoma', 40, 'bold'), fg='white', bg='black')
        test.place(x=300, y=100)

        hotelinfo.mainloop()