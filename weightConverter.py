from sqlite3 import converters


weight = int(input("Enter your weight: "))
unit = input("(L) or (K): ")
if unit.upper() == 'L':
    converted = weight * 0.45
    print(f"Your weight is {converted} kilos")
else:
    converted = weight / 0.45
    print(f"Your weight is {converted} pounds")