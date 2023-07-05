from tkinter import *
from tkinter.ttk import Combobox
from PIL import Image, ImageTk
from MENUFRAME import *

class MakeResFrame(Frame):
    def __init__(self, parent, res_list_frame):
        super().__init__(parent, bd=0, bg='#EEBA2B', width=830, height=475)
        self.place(x=322, y=211)
        self.res_list_frame = res_list_frame  # Store the ResListFrame instance

        test = Label(self, text="Make Reservation", font=('tahoma', 20, 'bold'), fg='white', bg='black')
        test.place(x=250, y=50)

        label1=Label(self, text='Name', font=('tahoma', 12, 'bold'), fg='black')
        label1.place(x=280, y=130, anchor='center')
        textbox1=Entry(self, fg='black', font=('tahoma', 12))
        textbox1.place(x=255, y=150)

        label2=Label(self, text='Date (mm/dd/yy)', font=('tahoma', 12, 'bold'), fg='black')
        label2.place(x=330, y=210, anchor='center')
        textbox2=Entry(self, fg='black', font=('tahoma', 12))
        textbox2.place(x=255, y=230)

        label3=Label(self, text='Room Type', font=('tahoma', 12, 'bold'), fg='black')
        label3.place(x=305, y=290, anchor='center')
        combo_box = Combobox(self)
        combo_box['values'] = ('Standard', 'Deluxe', 'Suite')
        combo_box.place(x=325, y=320, anchor='center')

        def save_data():
            name = textbox1.get()
            date = textbox2.get()
            room_type = combo_box.get()

            price_mapping = {
                'Standard': 3000,
                'Deluxe': 6000,
                'Suite': 10000
            }
            price = price_mapping.get(room_type, 0)

            filepath = "list.txt"
            tempFile = "temp.txt"

            room_id = self.res_list_frame.room_id_generator()  # Generate room_id

            try:
                with open(filepath, "a") as file:
                    file.write(f"{room_id},{name},{date},{room_type},{price}\n")
            except IOError as e:
                print("An error occurred while writing to the file:", e)

            # Update the table in the ResListFrame
            self.res_list_frame.update_table(room_id, name, date, room_type, price)

        button1 = Button(self, text='Add', fg='black', font=('tahoma', 14), command=save_data)
        button1.place(x=295, y=380, anchor='center')
