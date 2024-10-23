'''
class Employee:
  def printEmployeeDetails(self):
    print("Hello employee")
    print("Employee ID: ", self.employee_id)
    print("Employee Name: ", self.employee_name)
    print("Employee Type: ", self.type)
    
class Programmer(Employee):
  
  def printProgrammerDetails(self):
    super().printEmployeeDetails();
    print("Programming Language: ", self.language)
    print('Years of Experience: ', self.experience)
    
programmer = Programmer()
programmer.employee_id = 3
programmer.employee_name = "John"
programmer.type = "Software"
programmer.language = "Python"
programmer.experience = "Freasher"
programmer.printProgrammerDetails()
'''

class Employee:
    # Constructor to initialize employee details
    def __init__(self, employee_id, employee_name, emp_type):
        self.employee_id = employee_id
        self.employee_name = employee_name
        self.type = emp_type

    def printEmployeeDetails(self):
        print("Hello employee")
        print("Employee ID: ", self.employee_id)
        print("Employee Name: ", self.employee_name)
        print("Employee Type: ", self.type)
    
class Programmer(Employee):
    # Constructor to initialize both employee and programmer-specific details
    def __init__(self, employee_id, employee_name, emp_type, language, experience):
        # Call the parent class's constructor
        super().__init__(employee_id, employee_name, emp_type)
        # Initialize programmer-specific attributes
        self.language = language
        self.experience = experience
  
    def printProgrammerDetails(self):
        # Print employee details from the parent class
        super().printEmployeeDetails()
        # Print programmer-specific details
        print("Programming Language: ", self.language)
        print('Years of Experience: ', self.experience)

# Creating an instance of Programmer with all attributes
programmer = Programmer(employee_id=2, employee_name="Abhishek", emp_type="Software", language="Python", experience="Fresher")

# Printing programmer details
programmer.printProgrammerDetails()
