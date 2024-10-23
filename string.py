"""
manish = "Abhishek brother's has car"
course = 'I am now beginner "python" programmer'
# print(manish)
course = '''
Hi Abhishek,
Now you're learning python program
may be in 2 month you wil be expert
'''
course = 'Python for Beginners'
        # 012345
        # from left hand side indexing start with -1
# print(course[0])
print(course[0:3])
print(course[0:-19])
print(course[:])
print(course[2:4])
another = course[3:7]
print(another)

name = 'Abhishek'
print(name[1:-1])
first = 'Abhishek'
last = 'Gupta'
fullName = first + ' [' + last + '] is a coder'
print(fullName)
newName = f'{first} [{last}] is a coder'
print(newName)
"""
course = 'Python for beginners'
# print(len(course))
# course = course.upper()
# print(course.upper())
# print(course.lower())

# find will print the index of the string
# print(course.find('P'))
#print(course.find(' '))

#if any alphabet is not available in this case it will print -1
#print(course.find('z'))

#if we want to find the position of a word in a string it will print first position
# print(course.find('beginners'))

#print(course.replace('beginners', 'Expert'))
#print(course.replace('P', 'J'))

print('sython' in course)