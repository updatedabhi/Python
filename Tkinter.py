# Graphical tool kit for python
#Tkinter geometry method:
'''
1.Pack()
2.Grid()
3.Place()
'''
import tkinter
from tkinter import messagebox
from tkinter import *
top = Tk()
top.title("Abhishek")
#Pack() Module:
#button:
'''
b1 =  Button(top, text = 'Red', fg='Red', bg="White")
b1.pack(side=TOP)

b2 = Button(top, text='Blue', fg='blue', bg='white')
b2.pack(side=LEFT)

b3 = Button(top, text='Yellow', fg='yellow', bg="white")
b3.pack(side = RIGHT)

b4 = Button(top, text='Green', fg='Green', bg="white")
b4.pack(side = BOTTOM)

#Grid() Moduel:
#Table:
l1 = Label(top, text="Name")
l1.grid(row=0, column=0)
t1 = Entry(top)
t1.grid(row=0, column=1)
l2 = Label(top, text="Password")
l2.grid(row=1, column=0)
t2 = Entry(top)
t2.grid(row=1, column=1)
b1 = Button(top, text="submit", bg="pink")
b1.grid(row=3, column=0)

l1 = Label(top, text="Name")
l1.place(x = 10, y = 10)
t1 = Entry(top)
t1.place(x = 30, y = 10)
l2 = Label(top, text="password")
l2.place(x=20, y=20)
t2 = Entry(top)
t2.place(x=30, y=10)
l3 = Label(top, text="Email")
l3.place(x=30, y=30)
t3 = Entry(top)
t3.place(x=30, y=10)
b1 = Button(top, text="Submit")
b1.grid(row=0, column=4)
'''
def msg():
    messagebox.showinfo("Alert", "Submitted Successfully")
l1 = Label(top, text="RollNO")
l1.grid(row=0, column=0)
t1 = Entry(top)
t1.grid(row=0, column=1)
l2 = Label(top, text="name")
l2.grid(row=1, column=0)
t2 = Entry(top)
t2.grid(row=1, column=1)
b1 = Button(top, text="Submit", activeforeground="Yellow", activebackground="Green",command = msg)
b1.grid(row=3, column=0)
top.mainloop()






