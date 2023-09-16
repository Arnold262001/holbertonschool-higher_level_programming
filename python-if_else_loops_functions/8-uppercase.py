#!/usr/bin/python3
def uppercase(str):
    number = None
    lenStr = len(str)

    for i in range(lenStr):
        number = ord(str[i])

        if 97 <= number <= 122:
            number -= 32

        if i < lenStr - 1:
            print("{0}".format(chr(number)), end='')
    print("{0}".format(chr(number)))
