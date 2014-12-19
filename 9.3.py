#!/usr/bin/env python
# coding: utf8
seq = input()
seq = list(seq)
p = sum(seq)

def require(seq, length):
  """
  Возвращает True массив отрезков содержит в начале отрезки
  из которых можно составить в сумме отрезок длиной length
  не больше не меньше
  портит коллекцию seq
  """
  if length == 0: return True
  s = 0
  while len(seq) > 0:
    s += seq.pop(0)
    if s > length:
      return False
    elif s == length:
      return True

  return False

def can_complete(side_a_end, side_b, seq):
  # посчитали сколько должна быть другая сторона
  side_a = (p - side_b*2)/2
  if side_a*2 + side_b*2 != p:
    return False

  # идем по оставшимся отрезкам и собираем стороны
  seq = seq[:]
  if require(seq, side_a) and require(seq, side_b) and require(seq, side_a - side_a_end) and len(seq) == 0:
    return True
  else:
    return False

def make_rect(seq):
  for n1 in range(1, len(seq) - 2):
    side_a_end = sum(seq[:n1])
    for n2 in range(n1+1, len(seq) - 1):
      side_b = sum(seq[n1:n2])
      if can_complete(side_a_end, side_b, seq[n2:]):
        return True
  return False

print "YES" if make_rect(seq) else "NO"