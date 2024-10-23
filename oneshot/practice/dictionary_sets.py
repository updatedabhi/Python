# first question
hidi_dictionary = {
  "ghar": "House",
  "chutti": "holiday",
  "garmi": "summer",
  "pyar": "love"
}

word = input("Enter any hindi word: ")
result = hidi_dictionary.get(f"{word}")

if not result == None:
  print(f"The meaning of {word} is {result}")
else:
  print(f"Sorry, the word {word} is not in our dictionary.")
  
# second question
unique_numbers = set()

for i in range(8):
  num = int(input(f"Enter number {i+1}: "))
  unique_numbers.add(num)
  
print("Unique numbers are: ", unique_numbers)

# third question
my_set = {10, "10"}
print(my_set)

# fourth question
s = set()
s.add(20)
s.add(20.0)
s.add("20")

print(len(s))
