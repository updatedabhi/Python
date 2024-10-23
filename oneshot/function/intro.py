def percent(marks):
  return sum(marks) / 4

marks1 = [90, 85, 95, 80]
print(percent(marks1)) 

marks2 = [92, 34, 92, 52]
print(percent(marks2))

def updateList(l):
  l[0] = 100
  return l

l = [2, 5, 3, 0]
updateList(l)
print(l)

def greet(name = "Abhishek"):
  print("Hello, " + name + "!", end="")

greet("Sonam")
greet("Mahesh")

def incrememt_by_one(number):
  number = number + 1
  return number

number = 5;
print(incrememt_by_one(number))
print(number)

