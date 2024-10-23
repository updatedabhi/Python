time = int(input("Enter your time of parking in hour"))
c = 'car'
b = 'bus'
o = 'scooter'
category = input("Enter your vehicle category")

if category == c:
    print("you parked car")
    price = time * 10
    print("your amout", price)
elif category == b:
    print("you parked bus")
    price = time * 20
    print("your amout", price)
elif category == o:
    print("you parked other")
    price = time * 5
    print("your amout", price)
else:
    print("Service is unavaible")
