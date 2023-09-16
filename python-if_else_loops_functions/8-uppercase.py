#!/usr/bin/python3
def uppercase(str):
    n = [chr(ord(l) - 32) if 'a' <= l <= 'z' else l for l in str]
    print("{0}".format("".join(n)))
