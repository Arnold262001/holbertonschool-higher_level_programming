#!/usr/bin/python3
def remove_char_at(str, n):
    listStrNew = []

    for i in range(len(str)):
        if i != n:
            listStrNew.append(str[i])
    return "".join(listStrNew)
