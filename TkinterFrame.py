from tkinter import *
top = Tk()
top.geometry("140x100")
frame = Frame(top)
frame.pack()

leftFrame = Frame(top)
leftFrame.pack(side = LEFT)

rightFrame = Frame(top)
rightFrame.pack(side = RIGHT)

btn1 = Button(frame, text="Submit", fg="red", activebackground=("red"))
btn1.pack(side = LEFT)

btn2 = Button(frame, text="Remove", fg="Green", activebackground=("Green"))
btn2.pack(side = RIGHT)

btn3 = Button(frame, text="Add", fg="Brown", activebackground=("Brown"))
btn3.pack(side = LEFT)

btn4 = Button(frame, text="Update", fg="Yellow", activebackground=("Yellow"))
btn4.pack(side = RIGHT)

top.mainloop()
