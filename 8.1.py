#!/usr/bin/env python

class Comparator:
  def __init__(self, value):
    self.value = value

  def compare(self, other):
    if not hasattr(other, 'value'):
      return 1
    return cmp(self.value, other.value)
  