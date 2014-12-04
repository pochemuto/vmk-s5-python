#!/usr/bin/env python
from collections import *
words = raw_input().split()

counter = Counter()
positions = OrderedDict()
for pos, w in enumerate(words):
  positions[w] = pos
  counter[w] += 1

result = []
for word, pos in positions.items():
  count = counter[word]
  if count > 1:
    word += '(%d)' % pos
  result.append(word)

print ' '.join(result)