import tkinter
from tkinter import *
import os
import glob
from tkinter import filedialog

from gui import window, bottom_frame

global sixthbutton
global sixthlabel
global listofdirs
global listoffiles
global var1
global v
global x
global topframe6

topframe6 = Frame(window)
topframe6.pack(side=TOP)

listoffiles = []
listofdirs = []
listoflabels = []
sixthlabel1 = []
var1 = StringVar()
v = IntVar()
i = 0


def gotoseven():
    x = v.get()
    # print x
    # print listofdirs[x]
    # print listoffiles[x]
    topframe6.destroy()
    sixthbutton.destroy()
    exec(open(r"seven.py").read())


var = StringVar()
sixthlabel = Label(topframe6, textvariable=var, fg="red")
var.set("Select Text File:")
sixthlabel.pack()

# print sixthlabel1

currdir = os.getcwd()
tempdir = filedialog.askdirectory(parent=window, initialdir=currdir, title='Please select a directory')
if len(tempdir) > 0:
    print("You chose %s" % tempdir)

os.chdir(tempdir)
# for file in glob.glob("*.txt"):
# print file
# listoffiles.append(file)

for root, dirs, files in os.walk(tempdir):
    for file in files:
        if file.endswith(".txt"):
            if not file.endswith("summary.txt") and not file.endswith("abstract.txt"):
                listoffiles.append(file)
                listofdirs.append(os.path.join(root, file))
        # print os.path.join(root, file)

for file in listoffiles:
    Radiobutton(topframe6, text=file, variable=v, value=i).pack()
    i += 1

# print i
# print listofdirs
# print listoffiles


# sixthlabel1= Label( window, textvariable=var1 )
# var1.set(listoffiles)
# print var1.get()
# sixthlabel1.pack()


# for file in os.listdir("C:\Users\Varun\Desktop\Python"):
#    if file.endswith(".txt"):
#		listoffiles.append(file)
#		print file


# var1 = StringVar()
# sixthlabel1 = Label( window, textvariable=var1 )
# sixthlabel1.pack()


# print listoffiles
# print listofdirs
# print listoflabels

# for x in listoffiles, y in listoflabels:
#	y = Label( window, textvariable=var )
#	var.set(x)
#	y.pack()


sixthbutton = tkinter.Button(bottom_frame, text="SELECT", command=gotoseven)
sixthbutton.pack()
