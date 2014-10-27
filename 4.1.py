#!/usr/bin/env python

n = input()
s = input()

def add(n, start, seq, subsum):
  for i in xrange(start, len(seq)):
    value = subsum + seq[i]
    if value == n or (value < n and add(n, start+1, seq, value)):
      return True
  return False

print "YES" if add(n, 0, s, 0) else "NO"