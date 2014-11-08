#!/usr/bin/env python
# coding: utf
seq = raw_input().split()

ops = {
  '+': lambda y, x: x + y,
  '-': lambda y, x: x - y,
  '*': lambda y, x: x * y,
  '/': lambda y, x: x / y,
}

stack = []
try:
  for i in seq:
    if i in ops.keys():
      stack.append( ops[i]( stack.pop(), stack.pop() ) )
    else:
      stack.append(int(i))

  if len(stack) == 1:
    print stack[0]
  else:
    print "ERROR"
except:
  print "ERROR"
