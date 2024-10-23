income = int(input("Enter your income"))
if income < 150000:
    print("your amout after tax tax",income, "rupees")
elif (income < 300000) and (income > 150001):
    print("your amout after tax tax", (income * 10/100), "rupees")
elif (income < 500000) and (income > 300001):
    print("your amout after tax tax", (income * 20)/100, "rupees")
elif (income < 500000) and (income > 300001):
    print("your amout after tax tax", (income * 30)/100, "rupees")
else:
    print("thanks")
