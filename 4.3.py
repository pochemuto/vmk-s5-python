#!/usr/bin/env python
words = []
while True:
  line = raw_input()
  if line == "":
    break
  words += line.split()

stats = sorted(set(map(lambda w: (words.count(w), w), words)), reverse=True)
if len(stats) > 1 and stats[0][0] == stats[1][0]:
  print '---'
else:
  print stats[0][1]
