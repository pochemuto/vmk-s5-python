#!/usr/bin/env python
x1,y1,x2,y2,x3,y3,x4,y4 = input()
print "YES" if (x1-x2)*(y3-y4) == (y1-y2)*(x3-x4) else "NO"