#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i in matrix:
        strTmp = ''
        for o in i:
            strTmp = strTmp + str(o) + ' '
        print("{}".format(strTmp[:-1]))
