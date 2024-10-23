year = int(input("enter the year: "))
if (year % 400 == 0) or (year % 4 == 0 and year % 100!=0):
    print("Entered year is leap year")
else:
    print("Entered year is not leap year")
