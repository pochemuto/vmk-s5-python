#!/usr/bin/env python

class Vovel:
  allowed = set("aeiouy")

  def __getattr__(self, attr):
    if set(attr).issubset(self.allowed):
      return attr.upper()
    else:
      raise AttributeError("Vovel instance has no attribute '{}'".format(attr))


if __name__ == '__main__':
  A = Vovel()
  print A.aoao
  try:
    print A.field
  except AttributeError, msg:
    print "ERROR",msg