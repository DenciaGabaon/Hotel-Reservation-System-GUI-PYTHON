from msilib import Table
from tkinter import *
from PIL import Image, ImageTk
from tkinter.ttk import Treeview
from MENUFRAME import *

class ResListFrame(Frame):
    def __init__(self, parent):
        super().__init__(parent, bd=0, bg='#EEBA2B', width=830, height=475)
        self.place(x=322, y=211)

        test = Label(self, text="Reservation List", font=('tahoma', 20, 'bold'), fg='white', bg='black')
        test.place(x=250, y=50)

        # Create the Treeview widget for the table
        table = Treeview(self, columns=('Name', 'Date', 'Room Type', 'Price'))
        table.column('#0', width=0, stretch=NO)
        table.column('Name', anchor=W, width=150)
        table.column('Date', anchor=CENTER, width=100)
        table.column('Room Type', anchor=CENTER, width=100)
        table.column('Price', anchor=CENTER, width=100)

        # Create table headings
        table.heading('#0', text='', anchor=W)
        table.heading('Name', text='Name', anchor=W)
        table.heading('Date', text='Date', anchor=CENTER)
        table.heading('Room Type', text='Room Type', anchor=CENTER)
        table.heading('Price', text='Price', anchor=CENTER)

        # Read data from file and populate the table
        filepath = "list.txt"
        try:
            with open(filepath, "r") as file:
                for line in file:
                    data = line.strip().split(',')
                    if len(data) == 4:
                        name, date, room_type, price = data
                        table.insert('', 'end', text=name, values=(name, date, room_type, price))
        except FileNotFoundError:
            print(f"File '{filepath}' not found.")

        table.place(x=50, y=100)

        def update_table(self, name, date, room_type, price):
            self.table.insert('', 'end', text=name, values=(name, date, room_type, price))
