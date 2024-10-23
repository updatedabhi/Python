fruits = ['Banana', 'Watermelon', 'Cherry', 'Grapes']

for fruit in fruits:
  print(fruit)
  
print('second way')

for i in range(1, len(fruits), 2):
  print(fruits[i])
  
myDict = {
  'apple': 1,
  'banana': 2,
  'cherry': 3
}

for key in myDict:
  print(key)
  
for value in myDict.values():
  print(value)

for key, value in myDict.items():
  print(key, value)
  
  
name = "Abhishek"
for char in name:
  print(char)