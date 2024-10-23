from cProfile import label
from distutils.cmd import Command
import tkinter
from tkinter import *

top = Tk()

def hello():
    print("Hello")

#create a tolevel menu
menubar = Menu(top)
menubar.add_command(label="Hello", command = hello)
menubar.add_command(label="Quit", command=top.destroy)

top.config(menu=menubar)

top.mainloop()