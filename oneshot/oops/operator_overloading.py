# class Number:
#   def __init__(self, n):
#     self.n = n
    
#   def __add__(self, other):
#     return self.n + other.n
      
# n = Number(4)
# other = Number(9)

# sum = n + other
# print(sum)

# Two object addtion:
class ComplexAddition:
  def __init__(self, real, imag):
    self.real = real
    self.imag = imag
  
  def __add__(self, otherObject):
    return ComplexAddition(self.real + otherObject.real, self.imag + otherObject.imag)
  
  # def __str__(self):
  #   return f"{self.real} + {self.imag}i"
  
  def __repr__(self):
    return f"{self.real} + {self.imag}i"

obj1 = ComplexAddition(5, 7)
obj2 = ComplexAddition(2, 9)

complex_sum = obj1 + obj2

print(complex_sum)