def find_factorial(number):
  if number == 0 or number == 1:
    return 1
  else:
    return number * find_factorial(number - 1)
  
print(find_factorial(1))