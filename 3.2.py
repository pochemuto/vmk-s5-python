#!/usr/bin/env python
a = input()
print tuple(reversed(a[::2])) + tuple(a[1::2])
