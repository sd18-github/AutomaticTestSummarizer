import tkinter
from tkinter import *


# top = tkinter.Tk()
# Code to add widgets will go here...

def gotonext():
    # tkMessageBox.showinfo( "Plz wait", "Starting.....")
    label.destroy()
    gui_button.destroy()
    exec(open(r".\second.py").read())

# execfile(r"C:\Users\Nikhilesh\Documents\Ramaiah\FYP\ATS\second.py")

def close_window():
    window.destroy()


window = tkinter.Tk()
window.iconbitmap(default='1_icon.ico')
window.minsize(500, 600)
window.geometry("800x600")
window.geometry('+1+1')
window.title("ATS")

top_frame = Frame(window)
top_frame.pack(side=TOP)

bottom_frame = Frame(window)
bottom_frame.pack(side=BOTTOM)

# swin = ScrolledWindow(topframe, width=500, height=500)
# swin.pack()

var = StringVar()
label = Label(window, textvariable=var)
var.set("Welcome to ATS")
label.pack()

gui_button = tkinter.Button(bottom_frame, text="START", command=gotonext)
gui_button.pack()

exit_button = tkinter.Button(bottom_frame, text="EXIT", command=close_window)
exit_button.pack(side=BOTTOM)

window.mainloop()
# top.mainloop()
