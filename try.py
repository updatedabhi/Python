from tkinter import *
import tkinter.messagebox as tmsg
abhishek = Tk()
abhishek.title("Abhishek")

abhishek.geometry("500x400")
'''
#assigning min size
abhishek.minsize(34, 78)

#assingning max size
abhishek.maxsize(666, 777)
lbl = Label(text="Abhishek is good boy")
lbl.pack()

abhishek.geometry("737x437")
lbl = Label(text="pycharm", fg="blue", bg="yellow")
lbl.pack()

#Importing a photo in the label

for jpg image install (pip install pillow)
from PIL import Image, ImageTk
image = Image.open("file.jpg")
photo = ImageTk.PhotoImage(image)

photo = PhotoImage(file="string manipulation.png")
lbl = Label(image=photo)
lbl.pack()


lbl = Label(text="Abhishek",bg="Yellow", fg="pink", font=("Vardana", 78, BOLD), padx=34, pady=99, borderwidth=34, relief=GROOVE,)
lbl.pack(side=BOTTOM, fill=Y) #anchor="sw"
lbl = Label(text="Ready", background="Red",padx=1000)
lbl.pack(side=BOTTOM)

abhishek.minsize(400, 500)

#frame:

f1 = Frame(abhishek, bg="Yellow", borderwidth=5, relief=RIDGE, padx=145, pady=34)
f1.pack(side=TOP, fill='x')
lbl = Label(f1, text="Abhishek is good", bg="Yellow")
lbl.pack()

f2 = Frame(abhishek, bg="AliceBlue", borderwidth=5, relief=RIDGE, padx=155, pady=300)
f2.pack(fill=X)
lbl2 = Label(f2, text="I am good boy", bg="AliceBlue")
lbl2.pack()


#Button:
def hello():
    print("Hello Abhishke")

f = Frame(abhishek, borderwidth=6, bg="grey", relief=SUNKEN, padx=14)
f.pack(side=LEFT, anchor="nw")

lbl = Label(f, text="Click the button to get the desired service", bg="white")
lbl.pack(side=TOP)

btn = Button(f, fg="red", text="click me", command=hello)
btn.pack(side=LEFT, padx=0)
btn = Button(f, fg="Yellow", text="click me")
btn.pack(side=LEFT, padx=12)
btn = Button(f, fg="Green", text="click me")
btn.pack(side=LEFT, padx=12)
btn = Button(f, fg="Brown", text="click me")
btn.pack(side=LEFT)

def values():
    print(f"The customer username: {user_value.get()}")
    print(f"Ther cusotmer password: {password_value.get()}")


user = Label(abhishek, text="Username")
user.grid()
user_value = StringVar()
user_entry = Entry(abhishek, textvariable=user_value)
user_entry.grid(row=0, column=1)

password = Label(abhishek, text="Password")
password.grid(row=1, column=0)
password_value = StringVar()
password_entry = Entry(abhishek, textvariable=password_value)
password_entry.grid(row=1, column=1)

btn = Button(bg="skyBlue", text="Submit", command=values)
btn.grid()

#variable calsses in tkinter:
"""
#BooleanVar, DoubleVar, Intvar, stringVar
"""


def feedback():
    print("submitted successfully")
    print(f"{name_value.get(), phone_value.get(), gender_value.get(), emergency_value.get(), payment_value.get(), coder.get()}")

    with open("data.pdf", "a") as f:
        f.write(f"{name_value.get(), phone_value.get(), gender_value.get(), emergency_value.get(), payment_value.get(), coder.get()}\n")

Label(abhishek, text="Welcome to my CabService",pady=15, font="comicsansms 12 bold").grid(row=0, column=3)
name = Label(abhishek, text="Name")
phone = Label(abhishek, text="Phone")
gender = Label(abhishek, text="Gender")
emergency = Label(abhishek, text="Emergency Contact")
paymentmode = Label(abhishek, text="Payment Mode")

name.grid(row=1, column=2)
phone.grid(row=2, column=2)
gender.grid(row=3, column=2)
emergency.grid(row=4, column=2)
paymentmode.grid(row=5, column=2)

name_value = StringVar()
phone_value = StringVar()
gender_value = StringVar()
emergency_value = StringVar()
payment_value = StringVar()

name_entry = Entry(abhishek, textvariable=name_value)
phone_entry = Entry(abhishek, textvariable=phone_value)
gender_entry = Entry(abhishek, textvariable=gender_value)
emergency_entry = Entry(abhishek, textvariable=emergency_value)
payment_entry = Entry(abhishek, textvariable=payment_value)

name_entry.grid(row=1, column=3)
phone_entry.grid(row=2, column=3)
gender_entry.grid(row=3, column=3)
emergency_entry.grid(row=4, column=3)
payment_entry.grid(row=5, column=3)

coder = IntVar()
selecting_button = Checkbutton(text="Are You a developer", variable=coder)
selecting_button.grid(row=6, column=3)

btn = Button(abhishek, text="Submit", padx=39, command=feedback)
btn.grid(row=7, column=3, pady=4)


#canvas
canvas_widget = Canvas(abhishek, width=334, height=655)
canvas_widget.pack()

canvas_widget.create_rectangle(3, 8, 233, 134, fill="red")

#TODO: ABHISHEK IS GOOD BOY 

#menu & submenu
def func():
    print("Mujhe mt chhero")

my_menu = Menu(abhishek)
my_menu.add_command(label="File", command=func)

my_menu.add_command(label="Exit", command=exit)

abhishek.config(menu=my_menu)


def func():
    print("Mujhe mt chhero")
    tmsg.showinfo("alert", "your code submitted succefully")

def funct():
    value = tmsg.askquestion("alert", "Ary sure to exit?")
    if value == "no":
        tmsg.showinfo("alert", "pleaser save your project")

        

menubar = Menu(abhishek)
m1 = Menu(menubar, tearoff=0)
m1.add_command(label="New project", command=func)
m1.add_command(label="Save", command=funct)
m1.add_command(label="Save as", command=func)
m1.add_command(label="Print", command=func)
abhishek.config(menu=menubar)

menubar.add_cascade(label="File", menu=m1)
menubar.add_cascade(label="Exit", command=exit)


#slider:
def okay():
    tmsg.showinfo("alert", "we got it, you will be contact soon")
Label(abhishek, text="Show you interest in playing video game").pack()
slider = Scale(abhishek, from_=0, to=100, orient=HORIZONTAL, tickinterval=50)
slider.pack()

Button(abhishek, text="submit", padx=10, command=okay).pack()

#Radio Button:

def order():
    tmsg.showinfo("alert", "your order is successfylly ordered")

var = IntVar()
Label(abhishek, text="What's your choice sir?", font="lucida, 18 bold").pack()

radio_button = Radiobutton(abhishek, text="Dosa", padx=13, variable=var, value=1).pack(anchor="w")
radio_button = Radiobutton(abhishek, text="Noodles", padx=13, variable=var, value=2).pack(anchor="w")
radio_button = Radiobutton(abhishek, text="MoMo", padx=13, variable=var, value=3).pack(anchor="w")
radio_button = Radiobutton(abhishek, text="Pasta", padx=13, variable=var, value=4).pack(anchor="w")

Button(abhishek, text="Order Now", command=order).pack()
'''
lbx = Listbox(abhishek)
lbx.pack()

abhishek.mainloop()
