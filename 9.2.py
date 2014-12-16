from math import sqrt, pi

class Trigon:

  def __init__(self, a, b, c):
    self.a = a
    self.b = b
    self.c = c

  def perimeter(self):
    return self.a+self.b+self.c

  def square(self):
    a,b,c = self.a, self.b, self.c
    p = (a + b + c) / 2.0
    return sqrt(p*(p-a)*(p-b)*(p-c))

class Pea:

  def __init__(self, a, b, c):
    p = (a + b + c) / 2.0
    self.r = a*b*c/4/sqrt(p*(p-a)*(p-b)*(p-c))

  def square(self):
    return pi*self.r**2

  def perimeter(self):
    return 2*pi*self.r

class TrigonPea(Trigon, Pea):

  def __init__(self, a, b, c):
    Trigon.__init__(self, a, b, c)
    Pea.__init__(self, a, b, c)

  def volume(self):
    return self.perimeter() * Pea.square(self)
