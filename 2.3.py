#!/usr/bin/env python
s = input()
a = b = None
for n in s:
  if n>b:
    a,b = b,n
  elif n>a and n!=b:
    a = n
print a if a is not None else "NO"
