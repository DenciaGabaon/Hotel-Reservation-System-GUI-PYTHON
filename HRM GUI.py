from tkinter import *
from PIL import Image,ImageTk
from PIL import Image, ImageDraw

main_window = Tk()
main_window.title("Picadili Travels")
#main_window.attributes('-alpha', 0.7) # set color to transparent
main_window.config(bg='black')

# image declaration/ Load image
logo_img = PhotoImage(file='PicadiliLogo.png')


suite = (Image.open("suite.png"))
suite_resize = suite.resize((400, 500), Image.LANCZOS)
suite_img = ImageTk.PhotoImage(suite_resize)

name = (Image.open("Picadiliname.png"))
name_resize = name.resize((280, 60), Image.LANCZOS)
name_img  = ImageTk.PhotoImage(name_resize)

logox = (Image.open("Picadililogox.png"))
logox_resize = logox.resize((85, 85), Image.LANCZOS)
logox_img = ImageTk.PhotoImage(logox_resize)

#Makes the main window center
window_width = 800   # define window dimensions width and height
window_height = 500
screen_width = main_window.winfo_screenwidth()    # get the screen size of your computer
screen_height = main_window.winfo_screenheight()

position_top = int(screen_height / 2.5 - window_height / 2.5)  # Get the window position from the top dynamically
position_right = int(screen_width / 2 - window_width / 2)  # as well as position from left or right as follows

main_window.geometry(f'{window_width}x{window_height}+{position_right}+{position_top}') #this is the line that will center your window

#Log in Label

#login_label = Label(main_window, text="Welcome, Admin!",
 #                 font=('Tahoma', 25, 'bold'),
  #                fg='black', bg='yellow', padx= 250, pady= 30)
#login_label.place(x=50, y=9)

#Logo label
logo_label = Label(image=suite_img, borderwidth=0, highlightthickness=0)
logo_label.place(x=0, y=0)


#Logo canvas
logo_canvas = Canvas(main_window, width=400, height=125, borderwidth=0, highlightthickness=0)
logo_canvas.create_rectangle(0, 0, 400, 200, fill="#0D0D0D")
logo_canvas.place(x=0, y=165)
name_label = Label(image=name_img, borderwidth=0, highlightthickness=0, bg='#0D0D0D')
name_label.place(x=104, y=200)
logox_label = Label(image=logox_img, borderwidth=0, highlightthickness=0, bg='#0D0D0D')
logox_label.place(x=13, y=186)

#Log in canvas // UNFINISHED WORK
login_canvas = Canvas(main_window, width=400, height=400, borderwidth=0, highlightthickness=0)
login_canvas.create_rectangle(50, 50, 150, 100, radius=20, outline='black', fill='#272022')
login_canvas.place(x=180, y=100)

# Draw the rounded square

main_window.mainloop() #runs main_window


def round_rectangle(x1, y1, x2, y2, radius=25, **kwargs):
    points = [x1 + radius, y1,
              x1 + radius, y1,
              x2 - radius, y1,
              x2 - radius, y1,
              x2, y1,
              x2, y1 + radius,
              x2, y1 + radius,
              x2, y2 - radius,
              x2, y2 - radius,
              x2, y2,
              x2 - radius, y2,
              x2 - radius, y2,
              x1 + radius, y2,
              x1 + radius, y2,
              x1, y2,
              x1, y2 - radius,
              x1, y2 - radius,
              x1, y1 + radius,
              x1, y1 + radius,
              x1, y1]

    return login_canvas.create_polygon(points, **kwargs, smooth=True)



