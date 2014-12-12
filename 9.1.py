#!/usr/bin/env python

class MTuple:

  def __init__(self, *args, **params):
    self.__tuple = tuple(*args, **params)

  def __getattr__(self, name):
    attr = getattr(self.__tuple, name)

    if callable(attr):
      return self.__wrapper(attr)

    return attr

  def __to_tuple(self, value):
    if isinstance(value, MTuple):
      return value.__tuple
    else:
      return value

  def __wrapper(self, original):
    def wrapped(*args, **params):

      args = map(self.__to_tuple, args)
      params = {k: self.__to_tuple(v) for k,v in params.items()}

      result = original(*args, **params)
      if isinstance(result, tuple):
        result = MTuple(result)
      return result

    return wrapped

  def __neg__(self):
    return self[::-1]

if __name__ == '__main__':
  c = MTuple(range(10))
  print -(-c[2:6]+c[-1:2:-2])
  print -c[7:9]+("Bdyshch","Bdyshch")
  print {-c[3:5]:"QQ"}