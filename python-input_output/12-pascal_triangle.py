#!/usr/bin/python3
def pascal_triangle(n):
    if n <= 0:
        return []

    t = [[1 if ii <= 2 else ii for ii in range(
        1, i + 1)] for i in range(1, n + 1)]
    return t
