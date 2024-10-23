# from tkinter import *
'''
for i in 'python':
    print(i)
lst = ["Abhishek", 45, 88.34, True]
for item in lst:
    print(item)
for i in range(1, 11):
    print(i)
lst = [34, 38, 5343, 90]
sum = 0
for i in lst:
    sum = i + sum
print(f'Total: {sum}')
for x in range(4):
    for y in range(3):
        print(f'({x}, {y})')

for x in [5, 2, 5, 2, 2]:
    print('x' * x)
for x in [5, 2, 5, 2, 2]:
    output = ''
    for i in range(x):
        output += 'x'
    print(output)

names = ['Abhi', 'Ron', 'Sean', 'John']
print(names[0:-2])
numbers = [34, 32, 12, 89, 55]
max = numbers[0]
for i in numbers:
    if(max < i):
        max = i
print(max)

#list methods
numbers = [34, 56, 89, 56]
# numbers.append(90)
# numbers.insert(2, 0)
# numbers.remove(34)
# numbers.clear()
# numbers.pop()
# print(numbers.index(34))
# print(34 in numbers)
# print(numbers.count(56))
# numbers.sort()
# numbers.reverse()
# numbers.copy()
print(numbers)

nums = [3, 3, 3, 8, 9, 8]
uniques = []
for num in nums:
    if num not in uniques:
        uniques.append(num)
print(uniques)

#tuples
tpl = (34, 79, 'Abhishek')
# print(tpl[2])
# tpl[1] = 34 not possible
print(tpl)

#conpacking
name = ['Abhishek', 'John', 'Sohan']
a, b, c = name
print(a)

#dictionaries
student = {
    "name": "Abhishek Kumar",
    "age": 34,
    "is_good_at_coding": True
}
student["name"] = "Abhinav"
student["marks"] = 56
print(student)

Phone = input("Phone: ")
digits_mapping = {
    "1" : "One",
    "2" : "Two",
    "3" : "Three",
    "4" : "Four",
    "5" : "Five",
    "6" : "Six",
    "7" : "Seven",
    "8" : "Eight",
    "9" : "Nine"
}
output = ""
for ch in Phone:
    output += digits_mapping.get(ch, "") + " "
print(output)
'''



