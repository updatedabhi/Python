age = int(input("enter your age"))
if age < 18:
    print("sorry! your'e not eligible for vote")
    print("you will have to wait", 18 - age, "years")
else:
    print("welcome! you're eligeble for vote")
