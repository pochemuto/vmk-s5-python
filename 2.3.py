#!/usr/bin/env python
s = input()
b = None
for n in s:
  if n>b:
    a,b = b,n
print a if a is not None else "NO"
