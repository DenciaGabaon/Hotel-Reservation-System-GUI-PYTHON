from tkinter import *
from PIL import Image, ImageTk

class HotelInfoFrame(Frame):
    def __init__(self, parent):
        super().__init__(parent, bd=0, bg='#EEBA2B', width=830, height=475)
        self.place(x=322, y=211)

        test = Label(self, text="Hotel Information", font=('tahoma', 20, 'bold'), foreground='white', background='black')
        test.place(x=-40, y=50, anchor='w', width=900)

        # Load and display the image
        image_path3 = "suite.png"  # Replace with the actual image path
        image_path2 = "deluxe.jpg"  # Replace with the actual image path
        image_path1 = "standard.jpg"  # Replace with the actual image path
        self.load_image(image_path1, image_path2, image_path3)

    def load_image(self, image_path3, image_path2, image_path1):
        # Load the images using PIL
        image3 = Image.open(image_path3)
        image2 = Image.open(image_path2)
        image1 = Image.open(image_path1)

        # Resize the images to a smaller size
        smaller_image3 = image3.resize((180, 150), Image.LANCZOS)  # Adjust the size as needed
        smaller_image2 = image2.resize((180, 150), Image.LANCZOS)  # Adjust the size as needed
        smaller_image1 = image1.resize((180, 150), Image.LANCZOS)  # Adjust the size as needed

        # Create PhotoImage objects from the resized images
        photo3 = ImageTk.PhotoImage(smaller_image3)
        photo2 = ImageTk.PhotoImage(smaller_image2)
        photo1 = ImageTk.PhotoImage(smaller_image1)

        # Create labels to display the images
        image_label3 = Label(self, image=photo3, bd=0)
        image_label3.image = photo3  # Keep a reference to avoid garbage collection
        image_label3.place(x=60, y=161)  # Adjust the coordinates as needed

        image_label2 = Label(self, image=photo2, bd=0)
        image_label2.image = photo2  # Keep a reference to avoid garbage collection
        image_label2.place(x=310, y=161)  # Adjust the coordinates as needed

        image_label1 = Label(self, image=photo1, bd=0)
        image_label1.image = photo1  # Keep a reference to avoid garbage collection
        image_label1.place(x=560, y=161)  # Adjust the coordinates as needed

        header_label = Label(self, text="Hotel Picadili Travels, is a 15 Storey hotel in a vibrant commercial area. This sleek luxury hotel is 3 km from SM \n"
                                        "Mall of Asia, and 5 km from both World Trade Center Metro Manila and Ninoy Aquino International Airport. This Hotel\n"
                                        " serves a 24 hours reservation.",
                               font=('Sans', 10, 'bold'), fg='black', bg='#EEBA2B', justify='center')
        header_label.place(x=50, y=88)

        #ROOM TPYE
        standard_label = Label(self, text="Standard", width=23,
                               font=('Sans', 10, 'bold'), fg='white', bg='black', justify='center', padx=0, pady=0 )
        standard_label.place(x=57, y=306)

        deluxe_label = Label(self, text="Deluxe", width=23,
                             font=('Sans', 10, 'bold'), fg='black', bg='white', justify='center')
        deluxe_label.place(x=306, y=306)

        Suite_label = Label(self, text="Suite", width=23,
                            font=('Sans', 10, 'bold'), fg='white', bg='black', justify='center')
        Suite_label.place(x=556, y=306)



        #DESCRIPTION PER ROOM TYPE
        standard_label = Label (self,  text="40Sq-Meter\n Table and Queen Bed",
                               font=('Sans', 10, 'bold'), fg='black', bg='#EEBA2B', justify='center')
        standard_label.place(x= 67, y=356)

        deluxe_label = Label(self, text="60Sq-M, Sofa\n Table, and King Bed",
                               font=('Sans', 10, 'bold'), fg='black', bg='#EEBA2B', justify='center')
        deluxe_label.place(x= 326, y=356)

        Suite_label = Label(self, text="2Rooms, 120Sq-M\n Sofa and King Bed",
                               font=('Sans', 10, 'bold'), fg='black', bg='#EEBA2B', justify='center')
        Suite_label.place(x=580, y=356)


        #ROOM PRICE
        standard_label = Label(self, text="3000/24 Hours",
                               font=('Sans', 10, 'bold'), fg='black', bg='#EEBA2B', justify='center')
        standard_label.place(x=95, y=400)

        deluxe_label = Label(self, text="6000/24 Hours",
                             font=('Sans', 10, 'bold'), fg='black', bg='#EEBA2B', justify='center')
        deluxe_label.place(x=348, y=400)

        Suite_label = Label(self, text="10000/24 Hours",
                            font=('Sans', 10, 'bold'), fg='black', bg='#EEBA2B', justify='center')
        Suite_label.place(x=606, y=400)

