#!/usr/bin/env python

s = raw_input()
for i in range(1,len(s)/2+1):
  t = s[:i]
  r = len(s)/i
  if t*r == s:
    print r
    break
else:
  print 1