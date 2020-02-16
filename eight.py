import tkinter
from tkinter import *

from gui import bottom_frame, window

global file_name1
global file_src
global eighttext
global scrollbar
global file_name_exr
global gotonine
global file_name_abs
global eightbutton
global eightlabel
global eighttext
global eightlabel2
global eightlabel5
global eightlabel6
global scrollbar

var = StringVar()
var1 = StringVar()
var2 = StringVar()
var3 = StringVar()
var5 = StringVar()
var6 = StringVar()

eightlabel = Label(window, textvariable=var, fg="red")
var.set("Extractive Summary:")
eightlabel.pack()


def gotoabstractor():
    file_name2 = file_name1
    exec(open(r".\Abstractor.py").read())
    gotonine()


def gotonine():
    eightbutton.destroy()
    eightlabel.destroy()
    eighttext.destroy()
    eightlabel2.destroy()
    eightlabel5.destroy()
    eightlabel6.destroy()
    scrollbar.destroy()
    exec(open(r".\ninth.py").read())


file_name1 = file_src
exec(open(r".\Extractor.py").read())

file = open(file_name_exr, "r")
file_text = file.read()
# print file_text
file.close()

charCount = 0
words = file_text.split()
wordCount = len(words)
sentences = re.split(r' *[\.\?!][\'"\)\]]* *', file_text)
sentCount = len(sentences)
for word in words:
    for char in word:
        charCount += 1

# eightlabel1 = Label( window, textvariable=var1, wraplength=700)
# var1.set(file_text)
# eightlabel1.pack()

scrollbar = Scrollbar(window)
scrollbar.pack(side="right", fill="y")
eighttext = Text(window, yscrollcommand=scrollbar.set)
eighttext.insert(INSERT, file_text)
scrollbar.config(command=eighttext.yview)
eighttext.pack(side="left", fill="both")

eightlabel2 = Label(bottom_frame, textvariable=var2)
var2.set("Number of words: " + str(wordCount))
eightlabel2.pack(anchor=CENTER)

eightlabel5 = Label(bottom_frame, textvariable=var5)
var5.set("Number of sentences:" + str(sentCount))
eightlabel5.pack(anchor=CENTER)

eightlabel6 = Label(bottom_frame, textvariable=var6)
var6.set("Number of characters:" + str(charCount))
eightlabel6.pack(anchor=CENTER)

eightbutton = tkinter.Button(bottom_frame, text="ABSTRACTIVE SUMMARY", command=gotoabstractor)
eightbutton.pack()
