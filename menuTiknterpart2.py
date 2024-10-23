from cProfile import label
from tkinter import Toplevel, Button, Tk, Menu

top = Tk()
menubar = Menu(top)
file = Menu(menubar, tearoff=0)
file.add_command(label="New")
file.add_command(label="Open")
file.add_command(label="Save")
file.add_command(label="Save as...")
file.add_command(label="Close")

file.add_command(label="Exit", command=top.destroy)

file.add_separator()

menubar.add_cascade(label="File", menu=file)

edit = Menu(menubar, tearoff=1)
edit.add_command(label="Undo")
edit.add_command(label="Cut")
edit.add_command(label="Copy")
edit.add_command(label="Paste")
edit.add_command(label="Delete")
edit.add_command(label="Select All")
edit.add_separator()
menubar.add_cascade(label="Edit", menu=edit)
help = Menu(menubar, tearoff=2)
help.add_command(label="About")

menubar.add_cascade(label="Help", menu=help)

top.config(menu = menubar)

top.mainloop()