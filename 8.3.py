#!/usr/bin/env python

from math import sqrt

class Dot:

  def __init__(self, *coords):
    self.coords = coords

  def __str__(self):
    return ','.join(map(str, self.coords))

  def __len__(self):
    return len(self.coords)

  __repr__ = __str__

  def middle(self, other):
    if len(self) != len(other):
      raise ValueError()
    result = []
    for a, b in zip(self.coords, other.coords):
      result.append((a + b)/2.0)
    return Dot(*result)

  def distance(self, other):
    if len(self) != len(other):
      raise ValueError()
    acc = 0
    for a, b in zip(self.coords, other.coords):
      acc += (a - b)**2

    return sqrt(acc)

if __name__ == '__main__':
  for A,B in (Dot(1,2,3),Dot(3,4,5)), (Dot(1,2),Dot(3)):
    print A
    try:
      print "{:.3f}".format(A.distance(B))
      print A.middle(B)
    except ValueError:
      print "ERROR"