'''
number = int(input("Enter number: "))

for i in range(1, 11):
  print(f"{number} X {i} = {i * number}")
  
persons = ["Abhishek", "Abhinav", "Stuti", "Sonam", "Nikhil"]

for person in persons:
  if 'A' in person:
    print(f"Hello! Mr. {person}")
    
'''

number = int(input("Enter number: "))

if number == 1:
    print("1 is not a prime number")

elif number == 2:
    print("2 is a prime number")

else:
    for i in range(2, number):
        if number % i == 0:
            print(f"{number} is not a prime number")
            break
    else:
        print(f"{number} is a prime number")


  
