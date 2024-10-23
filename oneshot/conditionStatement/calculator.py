operator = input("Enter operator (+, -, *, /): ")
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))


if operator == '+':
  result = num1 + num2
elif operator == '-':
  result = num1 - num2
elif operator == '*':
  result = num1 * num2
elif operator == '/':
  result = num1 / num2
else:
  print("Invalid operator")
  
print(result)