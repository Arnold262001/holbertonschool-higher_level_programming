#!/usr/bin/python3
def remove_char_at(str, n):
    newStr = [str[c] for c in range(len(str)) if c != n]
    return "".join(newStr)
