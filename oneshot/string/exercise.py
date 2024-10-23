username = input("Enter username: ")

if len(username) > 12:
  print("Your username can't be more than 12 character")
elif not username.find(" ") == -1:
  print("Your username can't contain spaces")
elif not username.isalpha():
  print("Your username can't contain numbers")
else:
  print(f"Your username: {username}")