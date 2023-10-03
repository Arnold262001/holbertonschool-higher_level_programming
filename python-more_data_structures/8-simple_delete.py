#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    NO_EXITS = 'No existe'

    del_k = a_dictionary.get(key, NO_EXITS)

    if del_k != NO_EXITS:
        del a_dictionary[key]

    return a_dictionary
