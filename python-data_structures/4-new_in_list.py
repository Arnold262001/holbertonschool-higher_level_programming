#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    n = my_list[:]
    if idx >= 0 and idx < len(my_list):
        del(n[idx])
        n.insert(idx, element)
    return n
