from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
from HOTELINFO_FRAME import HotelInfoFrame
from MAKERES_FRAME import MakeResFrame
from RESLIST_FRAME import ResListFrame


def openframe1():
    hotelinfo_frame = HotelInfoFrame(menuWindow)
    menuWindow.mainloop()

def openframe2():
    makeres_frame = MakeResFrame(menuWindow)
    menuWindow.mainloop()

def openframe3():
    reslist_frame = ResListFrame(menuWindow)
    menuWindow.mainloop()

def logout():
    result = messagebox.askyesno("Logout Confirmation", "Are you sure you want to logout?")
    if result:
        menuWindow.destroy()

def exit():
    result = messagebox.askyesno("Exit Confirmation", "Are you sure you want to exit?")
    if result:
        menuWindow.destroy()


menuWindow = Tk()
menuWindow.overrideredirect(True)

# ========================Makes the window full screen and centered============================================
window_width = 1200
window_height = 720
screen_width = menuWindow.winfo_screenwidth()
screen_height = menuWindow.winfo_screenheight()

x_pos = int(screen_height / 2.5 - window_height / 3.4)  # Get the window position from the top dynamically
y_pos = int(screen_width / 2.34 - window_width / 2.07)  # as well as position from left or right as follows

menuWindow.geometry(f"{window_width}x{window_height}+{x_pos}+{y_pos}")
menuWindow.configure(background='black')

# Create a custom title bar
title_bar = Frame(menuWindow, bg='#EEBA2B', height=30)
title_bar.configure(height=38)
title_bar.pack(fill=X)

# Add title label to the title bar
title_label = Label(title_bar, text='Picadili Travels : Hotel Reservation System', fg='white', bg='#EEBA2B')
title_label.place(x=10, y=4)

# Add close button to the title bar
close_button = Button(title_bar, text='X', font=('Tahoma', 10, 'bold'), width=1, command=exit, bg='#EEBA2B')
close_button.pack(side=RIGHT)

# ===========Header===============================

header = (Image.open("header.png"))
header_resize = header.resize((920, 150), Image.LANCZOS)
header_img = ImageTk.PhotoImage(header_resize)
header_lbl = Label(menuWindow, image=header_img, borderwidth=0, highlightthickness=0, bg='black')
header_lbl.place(x=281, y=29)


# ========================================Button Frame==========================================
btn_frame = Frame(menuWindow, bd=0, bg='#0D0D0D')
btn_frame.place(x=0, y=29, width=280, height=690)

# ===============logo==============================
logo = (Image.open("PicadiliLogo.png"))
logo_resize = logo.resize((300, 290), Image.LANCZOS)
logo_img = ImageTk.PhotoImage(logo_resize)
logo_lbl = Label(btn_frame, image=logo_img, borderwidth=0, highlightthickness=0, bg='#0D0D0D')
logo_lbl.place(x=0, y=0)

HotelInfo_btn = Button(btn_frame, text="HOTEL INFORMATION", width=30, height=2, command=openframe1,
                       font=("Dialog", 13, "bold"), bg="#330201",
                       fg="white", bd=0, cursor="hand1")
HotelInfo_btn.place(x=0, y=320)


MakeRes_btn = Button(btn_frame, text="MAKE RESERVATION", width=30, height=2, justify='center',
                     font=("Dialog", 13, "bold"), bg="#330201", command=openframe2,
                     fg="white", bd=0, cursor="hand1")
MakeRes_btn.place(x=0, y=371)


ResList_btn = Button(btn_frame, text="RESERVATION LIST", width=30, height=2, justify='center',
                     font=("Dialog", 13, "bold"), bg="#330201", command=openframe3,
                     fg="white", bd=0, cursor="hand1")
ResList_btn.place(x=0, y=422)

LogOut_btn = Button(btn_frame, text="LOG OUT", width=30, height=2, justify='center', font=("Dialog", 13, "bold"),
                    bg="#330201", fg="white",
                    bd=0, cursor="hand1", command=logout)
LogOut_btn.place(x=0, y=473)

# ===============Main Frame========================
main_frame = Frame(menuWindow, bd=0)
main_frame.place(x=322, y=211, width=830, height=475)
main_frame.configure(background='#0D0D0D')

menuWindow.mainloop()
