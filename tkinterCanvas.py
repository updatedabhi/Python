'''
Canvas- draw graphs/pie-chart, shapes(arc, circle)
'''

from ast import Delete
from cgitb import text
from msilib.schema import ListBox
from pkgutil import extend_path
from textwrap import fill
import tkinter
from tkinter import *
from tracemalloc import start
from turtle import width

top = Tk()

top.geometry("300x1000")

#creating a simple canvas

c = Canvas(top, bg="pink", height="300")

c.pack()

#Cratin arc

c.create_arc((5, 10, 150, 200), start = 0, extent = 150, fill="yellow")

#checkButton:
checkvar1 = IntVar()

checkvar2 = IntVar()

checkvar3 = IntVar()

checkButton1 = Checkbutton(top, text="c", variable=checkvar1, onvalue=1, offvalue=0, height=2, width=10)

checkButton2 = Checkbutton(top, text="c++", variable=checkvar2, onvalue=1, offvalue=0, height=2, width=10)

checkButton3 = Checkbutton(top, text="Java", variable=checkvar3, onvalue=1, offvalue=0, height=2, width=10)

checkButton1.pack()

checkButton2.pack()

checkButton3.pack()

#list box:

listItem = Label(top, text="A list of favouriter countreis....")
listbox = Listbox(top)
listbox.insert(1, "India")
listbox.insert(2, "USA")
listbox.insert(3, "Japan")
listbox.insert(4, "Australia")

btn = Button(top, text="delete", command=lambda listbox = listbox:Delete(ANCHOR))

w = Menu()

listItem.pack()

listbox.pack()

btn.pack()

top.mainloop()