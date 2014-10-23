#!/usr/bin/env python

debug = False

if debug:
  from pprint import pprint

# input
lab = []
lab.append(list(raw_input()))
N = len(lab[0])
for i in xrange(1,N):
  lab.append(list(raw_input()))


def pr(lab):
  for i in range(N):
    print ''.join(map(lambda x: '##' if x == '#' else '..' if x == '.' else "%02d"%(x,), lab[i]))

if debug:
  pr(lab)

jumps = {}
s = 0
for i in range(N):
  for j in range(N):
    if lab[i][j] == '#':
      continue
    top = lab[i-1][j] if i > 0 else '#'
    left = lab[i][j-1] if j > 0 else '#'
    if left != '#':
      c = left
      if top != '#' and top != left:
        jumps[top] = [] if top not in jumps else jumps[top]
        jumps[top].append(left)
        jumps[left] = [] if left not in jumps else jumps[left]
        jumps[left].append(top)
    elif top != '#':
      c = top
    else:
      c = s
      s += 1
    lab[i][j] = c

start = lab[0][0]
end = lab[N-1][N-1]

if start == end:
  can = True
elif len(jumps) > 0:
  jumps[-1],jumps[start] = jumps[start],[-1]
  targets = jumps[start]
  i = 0
  while i < len(targets):
    cross = jumps[targets[i]]
    for t in cross:
      if t not in targets:
        if t == end:
          can = True
          break
        targets.append(t)
    else:
      i+=1
      continue
    break
  else:
    can = False
else:
  can = False

print "YES" if can else "NO"

if debug:
  print
  pr(lab)
  print
  pprint(jumps)
  print