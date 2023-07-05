from tkinter import *
from tkinter.ttk import Combobox
from PIL import Image, ImageTk
from MENUFRAME import *
from tkcalendar import DateEntry

class MakeResFrame(Frame):
    def __init__(self, parent, res_list_frame):
        super().__init__(parent, bd=0, bg='#EEBA2B', width=830, height=475)
        self.place(x=322, y=211)
        self.res_list_frame = res_list_frame  # Store the ResListFrame instance

        test = Label(self, text="Make Reservation", font=('tahoma', 20, 'bold'), foreground='white', background='black')
        test.place(x=0, y=50, anchor='w', width=900)

        label1=Label(self, text='Name', font=('tahoma', 12, 'bold'), fg='black')
        label1.place(x=350, y=130, anchor='center')
        textbox1=Entry(self, fg='black', font=('tahoma', 12))
        textbox1.place(x=325, y=150, width=180, height=25)

        label2 = Label(self, text='Date', font=('tahoma', 12, 'bold'), fg='black')
        label2.place(x=350, y=210, anchor='center')
        date_entry = DateEntry(self, font=('tahoma', 12), date_pattern='mm/dd/y')
        date_entry.place(x=325, y=230)

        label3=Label(self, text='Room Type', font=('tahoma', 12, 'bold'), fg='black')
        label3.place(x=375, y=290, anchor='center')
        combo_box = Combobox(self)
        combo_box['values'] = ('Standard', 'Deluxe', 'Suite')
        combo_box.place(x=415, y=320, anchor='center', width=180, height=25)

        def save_data():
            name = textbox1.get()
            date = date_entry.get_date().strftime('%m/%d/%y')
            room_type = combo_box.get()

            price_mapping = {
                'Standard': 3000,
                'Deluxe': 6000,
                'Suite': 10000
            }
            price = price_mapping.get(room_type, 0)

            filepath = "list.txt"

            room_id = self.res_list_frame.room_id_generator()  # Generate room_id

            try:
                with open(filepath, "a") as file:
                    file.write(f"{room_id},{name},{date},{room_type},{price}\n")
            except IOError as e:
                print("An error occurred while writing to the file:", e)

            # Update the table in the ResListFrame
            self.res_list_frame.update_table(room_id, name, date, room_type, price)

        button1 = Button(self, text='Add', fg='white', font=('tahoma', 14), command=save_data, cursor='hand1',bg="#420C09")
        button1.place(x=400, y=380, anchor='center', width=150)
