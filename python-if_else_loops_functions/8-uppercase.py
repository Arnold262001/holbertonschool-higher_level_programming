#!/usr/bin/python3
def uppercase(str):
    for i in str:
        number = int(ord(i))

        if 97 <= number <= 122:
            number -= 32

        if (len(str) - 1) != i:
            print("{0}".format(chr(number)), end='')
        else:
            print("{0}".format(chr(number)))
