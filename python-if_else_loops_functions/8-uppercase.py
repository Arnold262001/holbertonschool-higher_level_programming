#!/usr/bin/python3
def uppercase(str):
    lenStr = len(str)

    if lenStr != 0:
        for i in range(lenStr):
            number = ord(str[i])

            if 97 <= number <= 122:
                number -= 32

            if i < lenStr - 1:
                print("{0}".format(chr(number)), end='')
    else:
        number = 32
    print("{0}".format(chr(number)))
