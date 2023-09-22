#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix == [[]]:
        print()
    else:
        for i in matrix:
            u = 1
            for o in i:
                if u < len(i):
                    print("{} ".format(o), end='')
                else:
                    print("{}".format(o))
                u += 1
