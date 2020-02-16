import tkinter
from tkinter import *

from gui import window, bottom_frame

global thirdlabel
global thirdbutton
global thirdbutton1


def goback():
    thirdbutton.destroy()
    thirdbutton1.destroy()
    thirdlabel.destroy()
    exec(open(r".\fourth.py").read())


def gotosix():
    thirdbutton.destroy()
    thirdbutton1.destroy()
    thirdlabel.destroy()
    exec(open(r".\sixth.py").read())


# window = Frame(window)
# window.pack( side = TOP )

# bottom_frame = Frame(window)
# bottom_frame.pack( side = BOTTOM )

var = StringVar()
thirdlabel = Label(window, textvariable=var, fg="red")
var.set("Upload a file:")
thirdlabel.pack()

thirdbutton = tkinter.Button(bottom_frame, text="BROWSE", command=gotosix)
thirdbutton.pack()
thirdbutton1 = tkinter.Button(bottom_frame, text="BACK", command=goback)
thirdbutton1.pack()

# root.mainloop()
