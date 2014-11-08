#!/usr/bin/env python
# coding: utf
debug = False
string = raw_input()
start = maxlen = end = last_start = last_end = 0
chars = set()

for i,char in enumerate(string):
  if char in chars:
    # теперь подстрока будет начинаться с того места
    # перед которым был такой же символ как и char
    pos = string.index(char, last_start)
    cur_len = i - last_start
    if cur_len > maxlen:
      start = last_start
      maxlen = cur_len
      end = last_end
    
    last_start = pos + 1
    last_end = i + 1;
    chars = set(string[last_start:last_end])

  else:
    last_end+=1
    chars.add(char)

  if debug:
    print (" " * last_start) + string[last_start:i+1], i - last_start + 1

if len(string) - last_start > maxlen:
  if debug:
    print "> at end"
  start = last_start
  end = len(string)

print string[start:end]