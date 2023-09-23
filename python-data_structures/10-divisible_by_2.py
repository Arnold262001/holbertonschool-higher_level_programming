#!/usr/bin/python3
def divisible_by_2(my_list=[]):
      n = []
      if my_list != []:
            for i in range(len(my_list)):
                  if my_list[i] % 2 == 0:
                        n.insert(i, True)
                  else:
                        n.insert(i, False)
      return n
