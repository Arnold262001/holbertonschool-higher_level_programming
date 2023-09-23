#!/usr/bin/python3
def divisible_by_2(my_list=[]):
      n = []
      if len(my_list) > 0:
            for i, e in enumerate(my_list):
                  if e % 2 == 0:
                        n.insert(i, True)
                  else:
                        n.insert(i, False)
      return n
