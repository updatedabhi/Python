'''
# first question
fruits = []

for i in range(7):
  fruit = input(f"Enter fruit {i + 1}: ")
  fruits.append(fruit)

print(fruits)

# second question
marks = []
for i in range(6):
  mark = int(input(f"Enter mark {i + 1}: "))
  marks.append(mark)

marks.sort()

print(marks)

# third question
t = (2, 9, 0, 1)

# we can't do this because tuple is immutable
# t[0] = 3

print(t)

'''

# fourth question
nums = []
for i in range(4):
  num = int(input(f"Enter {i + 1} number: "))
  nums.append(num)

sum = 0
for num in nums:
  sum = sum + num

print(sum)

t = (1, 0, 0, 2, 0, 5)

result = t.count(0)

print(result)