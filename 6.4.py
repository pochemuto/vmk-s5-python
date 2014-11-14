#!/usr/bin/env python
# coding: utf
from types import ModuleType

module_name = raw_input()

try:
  module = __import__(module_name)
  count = 0
  for attr in dir(module):
    if type(getattr(module, attr)) == ModuleType:
      count+=1
  print count
except ImportError:
  print -1
