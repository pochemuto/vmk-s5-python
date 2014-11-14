#!/usr/bin/env python
# coding: utf 
stack = map(int, raw_input().split())

aux = None

def eq(stack):
  global aux
  aux = stack.pop()

ops = {
  '==': eq,
  '+': lambda s: s.append( s.pop() + s.pop() ),
  '-': lambda s: s.append( s.pop() - s.pop() ),
  # '*': lambda s: s.append( s.pop() * s.pop() ),
  # '/': lambda s: s.append( s.pop() / s.pop() )
}

ops_num = len(stack) - 1

def variations(items, count):
  if (count == 0):
    yield []
    return
  l = len(items)
  var = [0] * count
  while True:
    yield map(lambda n: items[n], var)

    
    if var[0] == l:
      break

    # считаем следующее значение
    for i in reversed(xrange(count)):
      var[i] += 1
      if var[i] == l:
        if i == 0:
          # перебор закончен - правая цифра перевалила
          return
        else:
          var[i] = 0
      else:
        break

def test(stack, op_seq):
  global aux # типа регистр в котором запоминаем значение справа от равно
  aux = None
  for op in op_seq:
    ops[op](stack)

  return stack[0] == aux

def printable(stack, op_seq):
  result = []
  for i, op in enumerate(op_seq):
    result.append(stack[i])
    result.append(op)
  result.append(stack[-1])
  return " ".join(map(str, result))

# перестановка знака =
found = False
for eq_pos in range(ops_num):
  if not found:
    for op_seq in variations("+-", ops_num-1):
      op_seq.insert(eq_pos, "==")
      # тут у нас есть последовательность операций и стек чисел
      # поехали проверять
      if eval(printable(stack, op_seq)):
        found = True
        break

print "YES" if found else "NO"