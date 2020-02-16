import tkinter
from tkinter import *

# import gui

# top = tkinter.Tk()
# Code to add widgets will go here...

# window = window
from tkinter import messagebox

from gui import window, bottom_frame

global var1
global radbutton1
global radbutton2
global secondlabel
global secondbutton
global retvar


def gotonext1():
    if var1.get() == 1:
        secondlabel.destroy()
        secondbutton.destroy()
        radbutton1.destroy()
        radbutton2.destroy()
        exec(open(r".\third.py").read())
    elif var1.get() == 2:
        retvar = 0
        # tkMessageBox.showinfo( "Plz wait", "Starting.....")
        secondlabel.destroy()
        secondbutton.destroy()
        radbutton1.destroy()
        radbutton2.destroy()
        exec(open(r".\fourth.py").read())

    # execfile(r"C:\Users\Nikhilesh\Documents\Ramaiah\FYP\ATS\fourth.py")


var1 = IntVar()

# topframe = Frame(window)
# topframe.pack( side = TOP)

# bottom_frame = Frame(window)
# bottom_frame.pack(side=BOTTOM)

# text = Text(window)
# text.insert(INSERT, "INPUT.....")
# text.pack()
var = StringVar()
secondlabel = Label(window, textvariable=var)
var.set("Choose input:")
secondlabel.pack()

# R1 = Radiobutton(root, text="Option 1", variable=var, value=1,command=sel)
# R1.pack( anchor = W )

radbutton1 = tkinter.Radiobutton(window, text="Upload a file", fg="red", variable=var1, value=1)
radbutton1.pack()
radbutton2 = tkinter.Radiobutton(window, text="Type text", fg="red", variable=var1, value=2)
radbutton2.pack()

# print var1

secondbutton = tkinter.Button(bottom_frame, text="SUBMIT", command=gotonext1)
secondbutton.pack()

# subbutton = tkinter.Button(bottom_frame, text ="SUBMIT" )
# subbutton.pack()
# blackbutton = tkinter.Button(bottom_frame, text="SUBMIT", fg="black")
# blackbutton.pack()


# window.mainloop()
# top.mainloop()
