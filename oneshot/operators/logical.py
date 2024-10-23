# logical OR

temp = -3
is_raining = False

if temp > 35 or temp < 0 or is_raining:
  print("The outdoor event is cancelled")
else:
  print("The outdoor event is still scheduled")
  
# logical AND
is_sunny = True
if (temp > 25 and is_sunny):
  print("This is HOT outside")
else: 
  print("This is COLD outside")
  
# logical NOT
is_sunny = False
if is_sunny:
  print("It is sunny")
elif temp < 0 and not is_sunny:
  print("It is cold and not sunny")
else:
  print("It is cold")