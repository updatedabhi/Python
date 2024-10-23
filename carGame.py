print("HelloWorld")
controlCommand = " "
started = True
stoped = True
while True:
    controlCommand = input("> ").lower()
    if controlCommand == "start":
        print("Car started...")
        if started:
            print("Car is already started")
        else:
            started = False
            print("Car is started...")

    elif controlCommand == "stop":
        print("Car stoped")

    elif controlCommand == "quit":
        break
    elif controlCommand == "help":
        print("""
start - to start car
stop - to stop car
quit - to quit
""")
    else:
        print("Sorry! i don't understand that")
