import tkinter
from tkinter import *

from gui import window, bottom_frame

global fifthlabel
global fifthbutton
global fifthlabel2
global fifthtext
global retvar
global file_src
global fifthlabel3
global fifthlabel5
global fifthlabel6
global fifthtext1
global scrollbar
global rat


def gotoeight():
    rat = fifthtext1.get("0.0", END)
    fifthlabel.destroy()
    fifthbutton.destroy()
    fifthlabel2.destroy()
    fifthtext.destroy()
    fifthlabel3.destroy()
    fifthlabel5.destroy()
    fifthlabel6.destroy()
    fifthtext1.destroy()
    scrollbar.destroy()
    exec(open(r".\eight.py").read())


# window = Frame(window)
# window.pack( side = TOP )

# bottom_frame = Frame(window)
# bottom_frame.pack( side = BOTTOM )
var = StringVar()
var1 = StringVar()
var2 = StringVar()
var3 = StringVar()
var5 = StringVar()
var6 = StringVar()

fifthlabel = Label(window, textvariable=var, fg="red")
var.set("Inserted Text:")
fifthlabel.pack()

# fifthlabel1 = Label( window, textvariable=var1 , wraplength=700)
# var1.set(input)
# fifthlabel1.pack()
scrollbar = Scrollbar(window)
scrollbar.pack(side="right", fill="y")
fifthtext = Text(window, yscrollcommand=scrollbar.set)
fifthtext.insert(INSERT, input)
scrollbar.config(command=fifthtext.yview)
fifthtext.pack(side="left", fill="both")

# scrollbar.config( command = fifthlabel1.yview )

# input= retrieve_input()

input_u = input.encode('utf-8', errors='ignore')
# print input_u
file_src = "written.txt"
file = open(file_src, "w")
file.write(input_u)
# file_text=file.read()
file.close()

file = open(file_src, "r")
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

fifthlabel2 = Label(bottom_frame, textvariable=var2)
var2.set("Number of words: " + str(wordCount))
fifthlabel2.pack(anchor=CENTER)

fifthlabel5 = Label(bottom_frame, textvariable=var5)
var5.set("Number of sentences:" + str(sentCount))
fifthlabel5.pack(anchor=CENTER)

fifthlabel6 = Label(bottom_frame, textvariable=var6)
var6.set("Number of characters:" + str(charCount))
fifthlabel6.pack(anchor=CENTER)

fifthlabel3 = Label(bottom_frame, textvariable=var3, justify=LEFT)
var3.set("RATIO:")
fifthlabel3.pack(anchor=CENTER)
fifthtext1 = Text(bottom_frame, height=1, width=5)
fifthtext1.pack(anchor=CENTER)

fifthbutton = tkinter.Button(bottom_frame, text="EXTRACTIVE SUMMARY", command=gotoeight)
fifthbutton.pack()
