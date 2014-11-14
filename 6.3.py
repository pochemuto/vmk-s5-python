#!/usr/bin/env python
# coding: utf
from pprint import pprint
main = None
details = {}
s = raw_input()
while s != "":
  line = s.split()
  name = line.pop(0)
  if main is None:
    main = name
  details[name] = line
  s = raw_input()


def build(partName):
  global details
  if partName not in details:
    return False
  else:
    v = details[partName]
    if type(v) is bool:
      return v
    else:
      v = details[partName] = all(map(build, v))
      return v

print  "YES" if build(main) else "NO"