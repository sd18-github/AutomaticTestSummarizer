import tkinter
from tkinter import *


global file_name_abs

var = StringVar()
var1 = StringVar()
var2 = StringVar()
var3 = StringVar()

nineabel = Label( window, textvariable=var ,fg="red")
var.set("Abstractive Summary:")
ninelabel.pack()

file=open(file_name_abs,"r")
file_text=file.read()
#print file_text
file.close()



words = file_text.split()
wordCount = len(words)

ninelabel1 = Label( window, textvariable=var1, wraplength=700)
var1.set(file_text)
ninelabel1.pack()


ninelabel2 = Label( window, textvariable=var2)
var2.set("Number of words: "+ str(wordCount))
ninelabel2.pack(anchor = CENTER)