from tkinter import *
from PIL import Image, ImageTk

def menu_window():
    menuWindow = Toplevel()
    menuWindow.title('Picadili Travels : Hotel Reservation System')

    # Make the menuWindow fullscreen
    window_width = 1300
    window_height = 720
    screen_width = menuWindow.winfo_screenwidth()
    screen_height = menuWindow.winfo_screenheight()
    x_pos = (screen_width // 2) - (window_width // 2)
    y_pos = (screen_height // 2) - (window_height // 2)
    menuWindow.geometry(f"{window_width}x{window_height}+{x_pos}+{y_pos}")

    menuWindow.configure(background='black')

    # ===============logo==============================
    img1=Image.open(r"C:\Users\dgcam\OneDrive - DepEd-NCR\Desktop\PYTHON FILES\HRM1\PicadiliLogo.png")
    # Create a black background image with the same size as the image
    background = Image.new("RGBA", img1.size, "black")
    # Paste the image onto the background
    image_with_background = Image.alpha_composite(background, img1)
    # Resize the image
    image_with_background = image_with_background.resize((230, 140), Image.ANTIALIAS)
    # Convert the image to a PhotoImage for Tkinter
    menuWindow.photoimg1 = ImageTk.PhotoImage(image_with_background)

    lblimg=Label(menuWindow, image=menuWindow.photoimg1, bd=4)
    lblimg.place(x=0, y=0, width=230, height=140)

    # ===============Main Frame========================
    main_frame=Frame(menuWindow, bd=4)
    main_frame.place(x=0,y=190,width=1550,height=620)
    main_frame.configure(background='gold')

    # ===============MENU==============================
    lbl_menu=Label(main_frame,text="MENU",font=("tahoma",20,"bold"),bg="dark red",fg="gold",bd=4)
    lbl_menu.place(x=0,y=0,width=280)

    # =============Button Frame========================
    btn_frame=Frame(main_frame,bd=4)
    btn_frame.place(x=0,y=35,width=280,height=170)
    btn_frame.configure(background='black')

    HotelInfo_btn=Button(btn_frame,text="HOTEL INFORMATION",width=22,font=("tahoma",14,"bold"),bg="dark red",fg="gold",bd=0,cursor="hand1")
    HotelInfo_btn.grid(row=0,column=0,pady=1)

    MakeRes_btn=Button(btn_frame,text="MAKE RESERVATION",width=22,font=("tahoma",14,"bold"),bg="dark red",fg="gold",bd=0,cursor="hand1")
    MakeRes_btn.grid(row=1,column=0,pady=1)

    ResList_btn=Button(btn_frame,text="RESERVATION LIST",width=22,font=("tahoma",14,"bold"),bg="dark red",fg="gold",bd=0,cursor="hand1")
    ResList_btn.grid(row=2,column=0,pady=1)

    LogOut_btn=Button(btn_frame,text="LOG OUT",width=22,font=("tahoma",14,"bold"),bg="dark red",fg="gold",bd=0,cursor="hand1")
    LogOut_btn.grid(row=3,column=0,pady=1)






    menuWindow.mainloop()
