#!/usr/bin/env python

class Vector:
  def __init__(self, x, y):
    self.x = x
    self.y = y

  def __str__(self):
    return "|{},{}|".format(self.x, self.y)

  def __add__(self, other):
    return Vector(self.x + other.x, self.y + other.y)

  def __mul__(self, other):
    if isinstance(other, Vector):
      return self.x*other.x + self.y*other.y
    else:
      return Vector(self.x*other, self.y*other)

  __rmul__ = __mul__
  __repr__ = __str__


if __name__ == '__main__':
  A = Vector(1,2)
  B = Vector(3,4)
  print A
  print A+B
  print A*B
  print 7*A