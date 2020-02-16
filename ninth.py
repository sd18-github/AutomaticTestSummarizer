import tkinter
from tkinter import *

from gui import window, bottom_frame

global file_name_abs
global ninelabel
global ninthtext
global ninelabel2
global ninelabel5
global ninelabel6
global ninthbutton
global scrollbar


def gotogui():
    ninelabel.destroy()
    ninelabel2.destroy()
    ninelabel5.destroy()
    ninelabel6.destroy()
    ninthbutton.destroy()
    ninthtext.destroy()
    scrollbar.destroy()
    exec(open(r".\second.py").read())


var = StringVar()
var1 = StringVar()
var2 = StringVar()
var3 = StringVar()
var5 = StringVar()
var6 = StringVar()

ninelabel = Label(window, textvariable=var, fg="red")
var.set("Abstractive Summary:")
ninelabel.pack()

file = open(file_name_abs, "r")
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

# ninelabel1 = Label( window, textvariable=var1, wraplength=700)
# var1.set(file_text)
# ninelabel1.pack()
scrollbar = Scrollbar(window)
scrollbar.pack(side="right", fill="y")
ninthtext = Text(window, yscrollcommand=scrollbar.set)
ninthtext.insert(INSERT, file_text)
scrollbar.config(command=ninthtext.yview)
ninthtext.pack(side="left", fill="both")

ninelabel2 = Label(bottom_frame, textvariable=var2)
var2.set("Number of words: " + str(wordCount))
ninelabel2.pack(anchor=CENTER)

ninelabel5 = Label(bottom_frame, textvariable=var5)
var5.set("Number of sentences:" + str(sentCount))
ninelabel5.pack(anchor=CENTER)

ninelabel6 = Label(bottom_frame, textvariable=var6)
var6.set("Number of characters:" + str(charCount))
ninelabel6.pack(anchor=CENTER)

ninthbutton = tkinter.Button(bottom_frame, text="RESTART", command=gotogui)
ninthbutton.pack()
