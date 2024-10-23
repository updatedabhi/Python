class Person:
  def __init__(self):
    print("Employee is created!")
  
  def __init__(self, name, age):
    self.name = name
    self.age = age
    
  def printDetails(self):
    print(f"Name: {self.name}, Age: {self.age}")
    
person1 = Person()
