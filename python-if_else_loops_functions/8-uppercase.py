#!/usr/bin/python3
def uppercase(str):
    for i in str:
        number = int(ord(i))

        if 65 <= number <= 90 or 48 <= number <= 57 or number == 32:
            print("{0}".format(chr(number)), end='')
        else:
            print("{0}".format(chr(number - 32)), end='')
