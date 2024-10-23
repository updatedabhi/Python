class Employee:
  salary = 5000
  
  # def changeSalary(self, sal):
  #   self.__class__.salary = sal
  
  def changeSalary(cls, sal):
    cls.salary = sal
    print(cls.salary)
  
  # @classmethod
  # def changeSalary(self, sal):
  #   self.salary = sal

employee = Employee()
employee.changeSalary(5392)
print(Employee.salary)