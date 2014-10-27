#!/usr/bin/env python
m,n = input()

result_padding = len(str(m*n))
first_padding  = len(str(n))

frmt = "{0:_>" + str(result_padding) + "}_=_{1:_>" + str(first_padding) + "}_*_{2}"
for x in range(1,n+1):
  print frmt.format(x*m,x,m)
