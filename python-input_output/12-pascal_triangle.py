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

    t = [[1 if ii <= 2 else ii for ii in range(
        1, i + 1)] for i in range(1, n + 1)]
    return t
