# inheritance: it allows a class to inherit attirbutes and method from another class

# Types of inheritance:
# 1. Single Inheritance: A class can inherit from only one class.
# 2. Multiple Inheritance: A class can inherit from more than one class.
# 3. Multilevel Inheritance: A class can inherit from another class which in turn

# single Inheritance
class Parent:
  a = 3
  
  def print_a(self):
    print(self.a)
  def something(self):
    print("Something is happening")

class Child(Parent):
  b = 5
  
  def sum(self):
    print(self.a + self.b)
    
  def something(self):
    print("addition is happening")

child = Child()
child.print_a()
print(Child.b)
child.something()
child.sum()
  
  
# multiple inheritance:
class Parent1:
  def print_a(self):
    print("Parent1")
    
class Parent2:
  def print_b(self):
    print("Parent2")

class Parent3:
  def print_c(self):
    print("Parent3")
    
class Child(Parent1, Parent2, Parent3):
  def print_d(self):
    print("Child")


child = Child()
child.print_a()
child.print_d()

# Multilevel inheritance
class GrandParent:
    def grandparent(self):
        print("Grandparent")

class Parent0(GrandParent):
    def parent0(self):
        print("Parent0")

class Child0(Parent0):
    def child0(self):
        print("Child0")

class SuperChild(Child0):
    def superchild(self):
        print("SuperChild")

superChild = SuperChild()

superChild.grandparent()  # Output: Grandparent
superChild.parent0()      # Output: Parent0
superChild.child0()       # Output: Child0
superChild.superchild()   # Output: SuperChild
