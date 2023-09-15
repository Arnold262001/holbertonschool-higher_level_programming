#!/usr/bin/python3
for i in range(90, 64, -1):
    number = i

    if number % 2 == 0:
        number += 32

    print(chr(number), end='')
