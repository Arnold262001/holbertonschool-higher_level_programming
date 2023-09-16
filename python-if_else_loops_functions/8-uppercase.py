#!/usr/bin/python3
def uppercase(str):
    newStr = []
    for letter in str:
        if 'a' <= letter <= 'z':
            letter = chr(ord(letter) - 32)
        newStr.append(letter)
    print("{0}".format("".join(newStr)))
