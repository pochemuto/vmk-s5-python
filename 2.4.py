#!/usr/bin/env python

x1,y1,r = input()
r2=r**2
points = input()
in_circle = True
for i in range(0,len(points),2):
  x2,y2 = points[i],points[i+1]
  if (x2-x1)**2+(y2-y1)**2 > r2:
    print "NO"
    break
else:
  print "YES"
