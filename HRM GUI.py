from tkinter import *
import tkinter as tk
import os
from PIL import Image, ImageTk
from PIL import Image, ImageDraw
from tkinter import messagebox

def open_menu():
    main_window.destroy()
    import MENUFRAME


def xor_encrypt_decrypt(data, key):
    encrypted_data = "".join(chr(ord(c) ^ key) for c in data)
    return encrypted_data


def login():
    username = entry_username.get()
    password = entry_password.get()

    file_path = "admin.txt"
    if os.path.isfile(file_path):
        # Read the encrypted credentials from the file
        with open("admin.txt") as fp:
            encrypted_username = fp.readline().strip()
            encrypted_password = fp.readline().strip()

        # print("username: ", encrypted_username) TEST
        # print("password: ", encrypted_password) TEST

        key = 73

        # Decrypt the message
        decrypted_user = xor_encrypt_decrypt(encrypted_username, key)
        decrypted_pass = xor_encrypt_decrypt(encrypted_password, key)

        # Check if the decrypted username and password match the entered values
        if decrypted_user == username and decrypted_pass == password:
            messagebox.showinfo("Login Successful", "Welcome, " + username + "!")
            open_menu()
        elif username == "admin" and password == "password":
            messagebox.showerror("Login Failed", "Invalid username or password")
        else:
            messagebox.showerror("Login Failed", "Invalid username or password")
    else:
        status_label.config(text="Credentials not found")


def on_username_focus_in(event):
    if entry_username.get() == "Username":
        entry_username.delete(0, END)
        entry_username.config(fg="black")


def on_username_focus_out(event):
    if entry_username.get() == "":
        entry_username.insert(0, "Username")
        entry_username.config(fg="gray")


def on_password_focus_in(event):
    if entry_password.get() == "Password":
        entry_password.delete(0, END)
        entry_password.config(show="*", fg="black")


def on_password_focus_out(event):
    if entry_password.get() == "":
        entry_password.insert(0, "Password")
        entry_password.config(show="", fg="gray")


def roundPolygon(x, y, sharpness, **kwargs):
    # The sharpness here is just how close the sub-points
    # are going to be to the vertex. The more the sharpness,
    # the more the sub-points will be closer to the vertex.
    # (This is not normalized)
    if sharpness < 5:
        sharpness = 5

    ratioMultiplier = sharpness - 1
    ratioDividend = sharpness

    # Array to store the points
    points = []

    # Iterate over the x points
    for i in range(len(x)):
        # Set vertex
        points.append(x[i])
        points.append(y[i])

        # If it's not the last point
        if i != (len(x) - 1):
            # Insert submultiples points. The more the sharpness, the more these points will be
            # closer to the vertex.
            points.append((ratioMultiplier * x[i] + x[i + 1]) / ratioDividend)
            points.append((ratioMultiplier * y[i] + y[i + 1]) / ratioDividend)
            points.append((ratioMultiplier * x[i + 1] + x[i]) / ratioDividend)
            points.append((ratioMultiplier * y[i + 1] + y[i]) / ratioDividend)
        else:
            # Insert submultiples points.
            points.append((ratioMultiplier * x[i] + x[0]) / ratioDividend)
            points.append((ratioMultiplier * y[i] + y[0]) / ratioDividend)
            points.append((ratioMultiplier * x[0] + x[i]) / ratioDividend)
            points.append((ratioMultiplier * y[0] + y[i]) / ratioDividend)
            # Close the polygon
            points.append(x[0])
            points.append(y[0])

            return canvas.create_polygon(points, **kwargs, smooth=TRUE)
            # return userlog.create_polygon(points, **kwargs, smooth=TRUE)


def close_window():
    main_window.destroy()


main_window = Tk()
main_window.overrideredirect(True)  # Remove window decorations
main_window.configure(bg='black')  # Set background color of the entire window

# Image declaration
suite = (Image.open("suite.png"))
suite_resize = suite.resize((400, 500), Image.LANCZOS)
suite_img = ImageTk.PhotoImage(suite_resize)

name = (Image.open("Picadiliname.png"))
name_resize = name.resize((280, 60), Image.LANCZOS)
name_img = ImageTk.PhotoImage(name_resize)

logox = (Image.open("Picadililogox.png"))
logox_resize = logox.resize((85, 85), Image.LANCZOS)
logox_img = ImageTk.PhotoImage(logox_resize)

# ========================Makes the main window center============================================
window_width = 800  # define window dimensions width and height
window_height = 500
screen_width = main_window.winfo_screenwidth()  # get the screen size of your computer
screen_height = main_window.winfo_screenheight()

position_top = int(screen_height / 2.5 - window_height / 2.5)  # Get the window position from the top dynamically
position_right = int(screen_width / 2 - window_width / 2)  # as well as position from left or right as follows

main_window.geometry(
    f'{window_width}x{window_height}+{position_right}+{position_top}')  # this is the line that will center your window

# Logo label
logo_label = Label(image=suite_img, borderwidth=0, highlightthickness=0)
logo_label.place(x=0, y=0)

# Create a custom title bar
title_bar = Frame(main_window, bg='#EEBA2B', height=30)
title_bar.configure(height=38)
title_bar.pack(fill=X)

# Add title label to the title bar
title_label = Label(title_bar, text='Picadili Travels : Hotel Reservation System', fg='white', bg='#EEBA2B')
title_label.place(x=10, y=4)

# Add close button to the title bar
close_button = Button(title_bar, text='X', font=('Tahoma', 10, 'bold'), width=1, command=close_window, bg='#EEBA2B')
close_button.pack(side=RIGHT)

# =================================use Images=======================================================
logo_canvas = Canvas(main_window, width=400, height=125, borderwidth=0, highlightthickness=0)
logo_canvas.create_rectangle(0, 0, 400, 200, fill="#0D0D0D")
logo_canvas.place(x=0, y=165)
name_label = Label(image=name_img, borderwidth=0, highlightthickness=0, bg='#0D0D0D')
name_label.place(x=104, y=200)
logox_label = Label(image=logox_img, borderwidth=0, highlightthickness=0, bg='#0D0D0D')
logox_label.place(x=13, y=186)

# ====================================Log in Frame===================================================
canvas = Canvas(main_window, width=310, height=380, borderwidth=0, highlightthickness=0, bg='black')
my_rectangle = roundPolygon([8, 300, 300, 8], [3, 3, 375, 375], 5, width=3, outline="#272022", fill="#272022")
canvas.place(x=445, y=73)

login_label = Label(main_window, text="Welcome, Admin!",
                    font=('Sans', 20, 'bold'),
                    fg='white', bg='#272022', padx=0, pady=0)
login_label.place(x=480, y=127)

userlog = Canvas(main_window, width=250, height=40, borderwidth=0, highlightthickness=0, bg='white')
# rectlog = roundPolygon([5, 100, 100, 5], [3, 3, 30, 30], 5, width=3, outline="#FFFFFF", fill="#FFFFFF")
userlog.place(x=473, y=190)

entry_username = Entry(main_window, width=38, fg="gray")
entry_username.config(relief=GROOVE, bd=0)
entry_username.insert(0, "Username")
entry_username.bind("<FocusIn>", on_username_focus_in)
entry_username.bind("<FocusOut>", on_username_focus_out)
entry_username.place(x=490, y=201)

passlog = Canvas(main_window, width=250, height=40, borderwidth=0, highlightthickness=0, bg='white')
# rectlog = roundPolygon([5, 100, 100, 5], [3, 3, 30, 30], 5, width=3, outline="#FFFFFF", fill="#FFFFFF")
passlog.place(x=473, y=255)

entry_password = Entry(main_window, width=38, fg="gray")
entry_password.config(relief=GROOVE, bd=0)
entry_password.insert(0, "Password")
entry_password.bind("<FocusIn>", on_password_focus_in)
entry_password.bind("<FocusOut>", on_password_focus_out)
entry_password.place(x=490, y=265)

button_login = Button(main_window, text="LOGIN", font=('Sans', 12, 'bold'), command=login, width=38, bg='#EEBA2B')
button_login.config(relief=GROOVE, bd=2, width=24)
button_login.place(x=473, y=350)

status_label = Label(main_window, text="", font=('Sans', 10), fg='Red', width=24, height=1, bg='#272022')
status_label.place(x=450, y=313)

main_window.mainloop()  # runs main_window
