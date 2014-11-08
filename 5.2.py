#!/usr/bin/env python
from itertools import islice, imap
x0,a,c,m = input()
y = input()

def random(a,c,m,x0):
  xn = x0
  yield x0
  while True:
    xnn = (a*xn + c) % m
    yield xnn
    xn = xnn

print "YES" if any(imap(lambda n: n == y, islice(random(a,c,m,x0), m))) else "NO"