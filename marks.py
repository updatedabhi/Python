marks = int(input("Enter your percentage"))
if marks > 75:
    print("you have passed with distinction")
elif (marks > 60) and (marks <= 75):
    print("you have passed with first class")
elif (marks < 50) and (marks <= 59.9):
      print("you have passed with second class")
elif (marks < 40) and (marks <= 49.9):
    print("you have passed with third class")
else:
    print("failed")
    
