import os
print(os.getcwd())

f = open('./fileHandling/sample.txt', 'r')
# data = f.read() it will read all content

data = f.read(5) # it will read first 5 char

print(data)
