#!/usr/bin/python3
def divisible_by_2(my_list=[]):
      n = []
      if my_list != []:
            for i in my_list:
                  if i % 2 == 0:
                        n += True
                  else:
                        n += False
      return n
