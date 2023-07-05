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
        smaller_image3 = image3.resize((200, 200))  # Adjust the size as needed
        smaller_image2 = image2.resize((200, 200))  # Adjust the size as needed
        smaller_image1 = image1.resize((200, 200))  # Adjust the size as needed

        # Create PhotoImage objects from the resized images
        photo3 = ImageTk.PhotoImage(smaller_image3)
        photo2 = ImageTk.PhotoImage(smaller_image2)
        photo1 = ImageTk.PhotoImage(smaller_image1)

        # Create labels to display the images
        image_label3 = Label(self, image=photo3, bd=0)
        image_label3.image = photo3  # Keep a reference to avoid garbage collection
        image_label3.place(x=50, y=150)  # Adjust the coordinates as needed

        image_label2 = Label(self, image=photo2, bd=0)
        image_label2.image = photo2  # Keep a reference to avoid garbage collection
        image_label2.place(x=300, y=150)  # Adjust the coordinates as needed

        image_label1 = Label(self, image=photo1, bd=0)
        image_label1.image = photo1  # Keep a reference to avoid garbage collection
        image_label1.place(x=550, y=150)  # Adjust the coordinates as needed
