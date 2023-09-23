#!/usr/bin/python3
def divisible_by_2(my_list=[]):
      n = []
      if my_list != [] and len(my_list) > 0:
            for i in my_list:
                  if type(i) == int:
                        if i % 2 == 0:
                              n.append(True)
                        else:
                              n.append(False)
            return n
