from tkinter import *
from tkinter import ttk
abhishek = Tk()

def func():
    to_value = cmb_value_to.get()
    from_value = cmb_value_from.get()
    if (to_value == "BH-1" and from_value == "MainGate") or (to_value == "MainGate" and from_value == "BH-1") or (to_value == "BH-1" and from_value == "Unihospital") or (to_value == "BH-1" and from_value == "Foodfactory") or (to_value == "Unihospital" and from_value == "BH-1") or (to_value == "Foodfactory" and from_value == "BH-1"):
        fare = "10 Rupees"
        print(f"You have to pay {fare}")
    elif (to_value == "BH-8" and from_value == "MainGate") or (to_value == "MainGate" and from_value == "BH-8") or (to_value == "BH-8" and from_value == "Unihospital") or (to_value == "BH-8" and from_value == "Foodfactory") or (to_value == "Unihospital" and from_value == "BH-8") or (to_value == "Foodfactory" and from_value == "BH-8"):
        fare = "10 Rupees"
        print(f"You have to pay {fare}")
    elif (to_value == "BH-2" and from_value == "MainGate") or (to_value == "MainGate" and from_value == "BH-2"):
        fare = "15 Rupees"
        print(f"You have to pay {fare}")
    elif (to_value == "BH-3" and from_value == "MainGate") or (to_value == "MainGate" and from_value == "BH-3"):
        fare = "20 Rupees"
        print(f"You have to pay {fare}")
    elif (to_value == "BH-4" and from_value == "MainGate") or (to_value == "MainGate" and from_value == "BH-4"):
        fare = "20 Rupees"
        print(f"You have to pay {fare}")
    elif (to_value == "BH-5" and from_value == "MainGate") or (to_value == "MainGate" and from_value == "BH-5"):
        fare = "25 Rupees"
        print(f"You have to pay {fare}")
    elif (to_value == "BH-6" and from_value == "MainGate") or (to_value == "MainGate" and from_value == "BH-6"):
        fare = "25 Rupees"
        print(f"You have to pay {fare}")
    elif (to_value == "BH-7" and from_value == "MainGate") or (to_value == "MainGate" and from_value == "BH-7"):
        fare = "30 Rupees"
        print(f"You have to pay {fare}")


abhishek.title("combobox")
abhishek.geometry("500x400")

lbl = Label(abhishek, text="To")
lbl.grid(row=0,column=0)
dest = ["BH-1", "BH-2", "BH-3", "BH-4", "BH-5", "BH-6", "BH-7", "BH-8", "Foodfactory", "MainGate", "Unihospital"]
cmb_value_to = StringVar()
cmb = ttk.Combobox(abhishek, values=dest, textvariable=cmb_value_to)
cmb.grid(row=0, column=2)

lbl2 = Label(abhishek, text="From")
lbl2.grid(row=1, column=0)

cmb_value_from = StringVar()
cmb2 = ttk.Combobox(abhishek, values=dest, textvariable=cmb_value_from)
cmb2.grid(row=1, column=2)

fare = Label(abhishek, text="Fare")
fare.grid(row=2, column=0)

fare_entry = Entry(abhishek, textvariable=fare.get())
fare_entry.grid(row=2, column=2)

btn = Button(abhishek, text="Book now", command=func)
btn.grid()


abhishek.mainloop()