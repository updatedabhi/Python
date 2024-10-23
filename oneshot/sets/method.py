a = set()
a.add(3)
a.add(6)
a.add(2)
a.add(2)
a.add(2)
# a.add([1, 5, 9]); this is not possible
a.add((2, 9, 9, 0))

# a.add({"name": "Abhishek"}) this is not possible because list and dictionary are not hashable

a.update([19, 92])

a.remove(2);

result = a.pop()
print(result)

for item in a:
  print(item)

a.clear()
print(a)

s1 = {2, 3, 5, 9}
s2 = {2, 5, 8, 1}

union = s1.union(s2)
print(union)

intersection = s1.intersection(s2)
print(intersection)
