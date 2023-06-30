from tkinter import *
from PIL import Image, ImageTk
from MENUFRAME import *

class HotelInfoFrame(Frame):
    def __init__(self, parent):
        super().__init__(parent, bd=0, bg='white', width=830, height=475)
        self.place(x=322, y=211)

        test = Label(self, text="test hotel info frame", font=('tahoma', 40, 'bold'), fg='white', bg='black')
        test.place(x=300, y=100)
