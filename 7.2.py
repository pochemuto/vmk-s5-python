#!/usr/bin/env python
from math import *
from itertools import product
form = raw_input()
scope = raw_input().split()

params = []
ranges = []
for p in scope:
  name, rng = p.split('=',2)
  bounds = rng.split(',')
  if len(bounds) > 1:
    values = range(int(bounds[0]), int(bounds[1]) + 1)
  else:
    values = [int(bounds[0])]
  params.append(name)
  ranges.append(values)

lambda_str = 'lambda %s: %s' % (','.join(params), form)
func = eval(lambda_str)

print max([func(*p) for p in product(*ranges)])