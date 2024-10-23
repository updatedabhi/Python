class Person:
  def __init__(self, name):
    self.name = name
  
  def get_name(self):
    print(self.name)
  
  def set_name(self, name):
    self.name = name
    
person = Person("Mohit")
person.get_name()
person.set_name("Chirag")
person.get_name()

# we can achieve similar thing by using property and we won't need to define function

class Student:
  def __init__(self, name):
    self._name = name
  
  @property
  def name(self):
    return self._name
  
  @name.setter
  def name(self, name):
    self._name = name
    
  name.deleter
  def name(self):
    del self._name
    
student = Student("Abhishek")
student.name = "Sangam"

del student.name
print(student.name)