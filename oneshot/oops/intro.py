# oops: using oops we model real world scenario into programming

# class: class is a blueprint which contain attribute, method of object.

# object: object is instance of class

# when a class is created no memory is allocated until object is created.

# self Keyword: The self keyword in Python is used to represent an instance (object) of a class. It allows you to access attributes and methods of the class

# in other word self keywrod refers current instace of class. it is used to access attribute and method of class.

#.When you define methods inside a class, the first parameter is always self, which represents the object that is calling the method.

class AirthmathicManipulation:
  def sum(self):
    return self.a + self.b;

airthmathicManipulation = AirthmathicManipulation()
airthmathicManipulation.a = 5
airthmathicManipulation.b = 10
print(airthmathicManipulation.sum())

class Employee:
  department = "IT department"
  def printDetails(self):
    print(f"Name: {self.name}")
    print(f"Role: {self.role}")
    print(f"Salary: {self.salray}")
    
employee1 = Employee()
employee1.name = "John"
employee1.role = "Python Developer"
employee1.salray = 5000
print(employee1.department)
employee1.printDetails()

employee2 = Employee()
employee2.name = "Manish"
employee2.experience = 5
print(employee2.experience)
# print(employee2.age) attribute error
