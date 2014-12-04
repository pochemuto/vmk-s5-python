#!/usr/bin/env python
from struct import pack, unpack
numbers = [int(v) for v in raw_input().split(',')]

bytes = ''
for n in numbers:
  bytes += pack('i', n)
# reverse
bytes = bytes[::-1]

print list(unpack('i' * len(numbers), bytes))