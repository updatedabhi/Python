'''

#list: list is mutable we can access it by its index and it is set of different data type
lst = [3, 6, 2, 9]
sorted_lst = lst.sort()
# print(sorted_lst)
lst[2] = 35
print(lst)


#tuple: tuple is immutable it is also set of different data type and it is also accessed by index
# inside tuple we can't apply methods
# usually it is used for constant use where the value of lst is not updatable
tpl = (34, 89, "Abhishek")
print(tpl[2])
print(tpl.count(34))
# print(tpl[0:2])
# tpl[1] = 34 it is not possible because tuple is immutable
print(tpl)

#store fruits name in a list from user

fruit1 = input("Enter fruit name: ")
fruit2 = input("Enter fruit name: ")
fruit3 = input("Enter fruit name: ")
fruit4 = input("Enter fruit name: ")
fruit5 = input("Enter fruit name: ")

my_fruit_list = [fruit1, fruit2, fruit3, fruit4, fruit5]

print(my_fruit_list)

m1 = int(input("Enter marks: "))
m2 = int(input("Enter marks: "))
m3 = int(input("Enter marks: "))
m4 = int(input("Enter marks: "))
m5 = int(input("Enter marks: "))

student_marks = [m1, m2, m3, m4, m5]
student_marks.sort()
print(student_marks)


numbers = [4, 8, 3, 10, 5]
sum = numbers[0]
for number in numbers:
    sum = sum + number
print(sum)

# from logging.config import dictConfig


dictonary = {
    "name": "Abhishek",
    "age": 34,
    "village": "Amgachhi",
    "marks": [34, 34, 89, 33],
    3: 345

}

# print(dictonary.keys())
# print(dictonary.values())
newlist = {
    "name": "Abishek"
}
dictonary.update(newlist)
# print(dictonary[3])
# print(dictonary)


#sets: in sets no repeative value is present set always stay inside parenthesis bracket
#set is collection of nonrepeatitive value
# a = {} this is a empty dictionary not a empty set

#we can't add list inside a set
# we can add tuple inside a set
# we cannot access it by its index

sets = {3, 3, 5, 3, 5, 8, "A"}
# sets.clear()
sets.pop()
print(len(sets))
sets.remove(3)
print(type(sets))
print(sets)

#playing with empty sets
b = set()
b.add(4)
b.add(34)
b.add((4, 34, "Abhishek"))
print(b)

hind_dictionary = {
    "Fan": "Phankah",
    "Dog": "Kutta",
    "Apple": "Seb"
}

print(hind_dictionary["Apple"])

print("Options are", hind_dictionary.keys())
a = input("Enter the english word: ")
print("The meaning of your word is: ", hind_dictionary[a])


#loop:

i = 1
while i < 78:
    print(str(i))
    i += 1

fruits = ['Watermelon', 'Mango', 'Banana', 'Grapes']

i = 0
while i < len(fruits):
    print(fruits[i])
    i = i + 1

result = [3, 8, 9, 0, 4]
for marks in result:
    print(marks)

#for loop using range
for i in range(0, 11):
    print(i)

for i in range(1, 34, 2):
    print(i)


for i in range(10):
    print(i)
    if i == 5:
        break

for i in range(10):
    # print(i)
    if i == 5:
        continue
    print(i)


for i in range(31):
    if i % 2 != 0:
        continue
    print(i)


for i in range(10):
    if i > 4:
        pass
    print(i)


n = int(input("Enter the number: "))
for i in range(1, 11):
    # print((i * n))
    print(f'{i} x {n} = {i * n}')


names = ['Abhishek', 'Sohan', 'Mohan', 'Sonu']
for name in names:
    if name.startswith("S"):
        print(name, "Good morning")

# Given number is prime Number or not
number = int(input("Enter the number: "))
is_prime_number = True
for i in range(2, number):
    if (number % i == 0):
        is_prime_number = False
        break
if is_prime_number:
    print(number, "is primer number")
else:
    print(number, "is not Primer Number") 



#Factorial of any number

number = int(input("Enter the number: "))
fact = 1
for divisor in range(1, number + 1):
    fact = fact * divisor
print(fact)


iteration = int(input("Enter the iteration: "))
for i in range(1, iteration + 1):
    print(i * "*")


#function in python:
marks = [34, 80, 00, 23, 45]
print(len(marks))
def result(marks):
    return sum(marks) / len(marks)

result()
'''
