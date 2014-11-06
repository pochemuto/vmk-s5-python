#!/usr/bin/env python

a = input()
a = list(a) if type(a) is tuple else [a]

s = input()
for i,n in enumerate(a):
  if i < s:
    a[i] = (n, [0])
  else:
    prev_jump = min(a[i-s:i])
    a[i] = (n + prev_jump[0], prev_jump[1] + [i])

print a[-1][0]