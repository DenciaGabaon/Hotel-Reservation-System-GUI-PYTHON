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
        test.place(x=-70, y=50, anchor='w', width=900)

        # Create the Treeview widget for the table
        self.table = Treeview(self, columns=('Room ID', 'Name', 'Date', 'Room Type', 'Price'))
        self.table.column('#0', width=0, stretch=NO)
        self.table.column('Room ID', anchor=W, width=100)
        self.table.column('Name', anchor=W, width=100)
        self.table.column('Date', anchor=CENTER, width=100)
        self.table.column('Room Type', anchor=CENTER, width=100)
        self.table.column('Price', anchor=CENTER, width=100)

        # Create table headings
        self.table.heading('#0', text='', anchor=W)
        self.table.heading('Room ID', text='Room ID', anchor=W)
        self.table.heading('Name', text='Name', anchor=W)
        self.table.heading('Date', text='Date', anchor=CENTER)
        self.table.heading('Room Type', text='Room Type', anchor=CENTER)
        self.table.heading('Price', text='Price', anchor=CENTER)

        # table center
        self.table.place(relx=0.4, rely=0.3, anchor='center')

        # Read data from file and populate the table
        filepath = "list.txt"
        try:
            with open(filepath, "r") as file:
                for line in file:
                    data = line.strip().split(',')
                    print(data)  # Print data for debugging
                    if len(data) == 5:
                        room_id, name, date, room_type, price = data
                        self.table.insert('', 'end', text=room_id, values=(room_id, name, date, room_type, price))
        except FileNotFoundError:
            print(f"File '{filepath}' not found.")

        self.table.place(x=50, y=100)

    def update_table(self, name, date, room_type, price):
        room_id = self.room_id_generator()  # Generate room_id
        self.table.insert('', 'end', text=room_id, values=(room_id, name, date, room_type, price))

    @staticmethod
    def room_id_generator():
        try:
            with open("list.txt", "r") as file:
                lines = file.readlines()
                if lines:
                    last_line = lines[-1].strip()
                    last_room_id = int(last_line.split(',')[0])
                    room_id = last_room_id + 1
                else:
                    room_id = 1
        except FileNotFoundError:
            room_id = 1

        return room_id
