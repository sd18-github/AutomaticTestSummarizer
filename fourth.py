import tkinter
from tkinter import *

from gui import bottom_frame, window

global fourthlabel
global fourthbutton
global fourthtext
global input
global scrollbar


def gotofive():
    input = fourthtext.get("0.0", END)
    fourthbutton.destroy()
    fourthlabel.destroy()
    fourthtext.destroy()
    scrollbar.destroy()
    exec(open(r".\fifth.py").read())


var = StringVar()
fourthlabel = Label(window, textvariable=var, fg="red")
var.set("Enter Text:")
fourthlabel.pack()

scrollbar = Scrollbar(window)
scrollbar.pack(side="right", fill="y")
fourthtext = Text(window, yscrollcommand=scrollbar.set)
fourthtext.insert(INSERT, "INPUT TEXT.")
scrollbar.config(command=fourthtext.yview)
fourthtext.pack(side="left", fill="both")

fourthbutton = tkinter.Button(bottom_frame, text="SUBMIT", command=gotofive)
fourthbutton.pack()
