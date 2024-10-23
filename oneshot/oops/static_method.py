class Employee:
  company = "Google"
  def getDetails(self):
    print(f"Name: {self.name}\nAge: {self.age}\nAddress: {self.address}")
  
  def introduce_yourself(self, name):
    print(f"Hello {name}! I am {self.name}.")

  @staticmethod
  def greet():
    print("Hello, I am an employee of Google!")
    
employee = Employee()
employee.name = "John"
employee.age = 30
employee.address = "New York"
employee.introduce_yourself("Yamada")

employee.getDetails()
Employee.greet()