#!/usr/bin/python3
def uppercase(str):
    o = 0

    if str != "":
        for i in str:
            number = int(ord(i))

            if 97 <= number <= 122:
                number -= 32

            if (len(str) - 1) != o:
                print("{0}".format(chr(number)), end='')
            else:
                break
            o += 1

    print("{0}".format(chr(number)))
