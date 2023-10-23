#!/usr/bin/python3
"""
Este módulo define la función pascal_triangle.
"""


def pascal_triangle(n):
    """
    Esta función regresa el triángulo de pascal.

    Args:
        n (int): Número de filas en el triángulo.
    Returns:
        list: Regresa una lista de lista con el triángulo.
    """
    if n <= 0:
        return []

    t = [[1]]

    for i in range(1, n):
        fila = [1]
        for j in range(1, i):
            fila.append(t[i-1][j-1] + t[i-1][j])
        fila.append(1)
        t.append(fila)

    return t
