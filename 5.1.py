#!/usr/bin/env python
from math import *
f = eval('lambda x:' + raw_input())
a,b = input()

def gen():
  for i in xrange(a,b+1):
    try:
      yield f(i)
    except:
      continue


print min(gen()), max(gen())