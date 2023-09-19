#!/usr/bin/python3
from sys import argv

if __name__ == '__main__':
    lenArgc = len(argv) - 1

    if lenArgc == 0:
        print("{} arguments.".format(lenArgc))
    else:
        print("{} arguments:".format(lenArgc))

        for i in range(1, lenArgc + 1):
            print("{0}: {1}".format(i, argv[i]))
