#!/usr/bin/env python
print ' '.join(sorted(raw_input().split(), key=lambda w: len(set(w))))