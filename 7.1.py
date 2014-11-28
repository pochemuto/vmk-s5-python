#!/usr/bin/env python
import string

K, N = input()

def to_base(value, base):
  if value == 0:
    return '0'
  chars = string.digits + string.uppercase
  negative = value < 0
  if negative:
    value *= -1
  result = ''
  while value > 0:
    result = chars[value % base] + result
    value /= base
  if negative:
    result = '-' + result
  return result

for n in xrange( N ** (K - 1), N ** K):
  print to_base(n, N)