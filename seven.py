import tkinter
from tkinter import *
import os
import re
import glob

from gui import window, bottom_frame
from sixth import listofdirs, x

global sevenbutton
global sevenlabel
global sevenlabel1
global sevenlabel2
global sevenlabel3
global sevenlabel5
global sevenlabel6
global file_src
global secondtext
global rat
global sevenlabel4
global seventext
global scrollbar


def gotoeight():
    rat = secondtext.get("0.0", END)
    sevenlabel.destroy()
    sevenlabel1.destroy()
    seventext.destroy()
    sevenlabel3.destroy()
    sevenlabel5.destroy()
    sevenlabel6.destroy()
    sevenbutton.destroy()
    secondtext.destroy()
    sevenlabel4.destroy()
    scrollbar.destroy()
    exec(open(r".\eight.py").read())

var = StringVar()
var1 = StringVar()
var2 = StringVar()
var3 = StringVar()
var4 = StringVar()
var5 = StringVar()
var6 = StringVar()

sevenlabel = Label(window, textvariable=var, fg="red")
var.set("The selected file is: ")
sevenlabel.pack()

# print x
# print listofdirs[x]
# print listoffiles[x]

try:
    file = open(listofdirs[x], "r")
except IOError:
    print("There was an error reading file")
    sys.exit()
file_text = file.read()
file.close()
# print file_text
sevenlabel1 = Label(window, textvariable=var1)
file_src = file.name
var1.set(file_src)
sevenlabel1.pack()

# sevenlabel2 = Label( window, textvariable=var2, wraplength=700)
# var2.set(file_text)
# sevenlabel2.pack()

scrollbar = Scrollbar(window)
scrollbar.pack(side="right", fill="y")
seventext = Text(window, yscrollcommand=scrollbar.set)
seventext.insert(INSERT, file_text)
scrollbar.config(command=seventext.yview)
seventext.pack(side="left", fill="both")

charCount = 0
words = file_text.split()
wordCount = len(words)
sentences = re.split(r' *[.?!][\'")\]]* *', file_text)
sentCount = len(sentences)
for word in words:
    for char in word:
        charCount += 1

sevenlabel3 = Label(bottom_frame, textvariable=var3)
var3.set("Number of words:" + str(wordCount))
sevenlabel3.pack(anchor=CENTER)

sevenlabel5 = Label(bottom_frame, textvariable=var5)
var5.set("Number of sentences:" + str(sentCount))
sevenlabel5.pack(anchor=CENTER)

sevenlabel6 = Label(bottom_frame, textvariable=var6)
var6.set("Number of characters:" + str(charCount))
sevenlabel6.pack(anchor=CENTER)

sevenlabel4 = Label(bottom_frame, textvariable=var4, justify=LEFT)
var4.set("RATIO:")
sevenlabel4.pack(anchor=CENTER)

secondtext = Text(bottom_frame, height=1, width=5)
secondtext.pack(anchor=CENTER)
# secondtext.insert(topframe,"per")
# scrollbar.config( command = fourthtext.yview )


sevenbutton = tkinter.Button(bottom_frame, text="EXTRACTIVE SUMMARY", command=gotoeight)
sevenbutton.pack()
