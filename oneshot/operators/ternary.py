num = 4

print("Positive" if num > 0 else "Negative")

result = "Even" if num % 2 == 0 else "Odd"

print(result)

a = 3
b = 7
max_num = a if a > b else b
print(max_num)

min_num = a if a < b else b
print(min_num)

user_role = "user"
access_level = "Full access" if user_role == "admin" else "Limited access"
print(access_level)