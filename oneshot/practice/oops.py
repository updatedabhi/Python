'''
class C2dvector:
  def __init__(self, x, y):
    self.x = x
    self.y = y
  
  def __repr__(self):
    return f"{self.x}x + {self.y}y"

class C3dvector(C2dvector):
  def __init__(self, x, y, z):
    super().__init__(x, y)
    self.z = z

tow_d_vector = C2dvector(5, 9)
print(tow_d_vector)

three_d_vector = C3dvector(2, 1, 7)
print(three_d_vector)


class Animal:
  def __init__(self, name, age):
    self.name = name
    self.age = age
  
  def sounds(self):
    print("Animal makes some sound")

class Dog(Animal):
  def __init__(self, name, age):
    super().__init__(name, age)
  
  def sounds(self):
    print(f"{self.name} is barking")
    
dog = Dog("Pitbull", 34)
dog.sounds()



class Complex:
  def __init__(self, real, imag):
    self.real = real
    self.imag = imag
  
  def __add__(self, obj2):
    return Complex(self.real + obj2.real, self.imag + obj2.imag)
  
  def __mul__(self, obj2):
    return Complex(self.real * obj2.real, self.imag * obj2.imag)
  
  def __repr__(self):
    return f"{self.real} + {self.imag}i"
  
obj1 = Complex(2, 5)
obj2 = Complex(3, 7)

print(obj1 * obj2)
print(obj1 + obj2)

'''