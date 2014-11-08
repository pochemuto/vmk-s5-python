#!/usr/bin/env python
# coding: utf
seq = raw_input().split()

ops = {
  '+': lambda x, y: x + y,
  '-': lambda x, y: x - y,
  '*': lambda x, y: x * y,
  '/': lambda x, y: x / y,
}

stack = []
try:
  for i in seq:
    if i in ops.keys():
      b = stack.pop()
      a = stack.pop()
      stack.append( ops[i]( a, b ) )
    else:
      stack.append(int(i))

  print stack[0]
except:
  print "ERROR"
