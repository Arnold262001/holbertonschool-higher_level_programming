#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if my_list != None and len(my_list) > 0:
        my_list.reverse()
        for i in my_list:
            print("{}".format(i))
