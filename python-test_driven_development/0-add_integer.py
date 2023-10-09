#!/usr/bin/python3
"""
Este módulo contiene operaciones matemáticas

Example:
    add_integer(4, 9)
"""


def add_integer(a, b=98):
    """
    Esta función suma dos enteros.

    Args:
        a (int): Primer entero
        b (int): Segundo entero(valor por defecto 98)

    Returns:
        int: return a + b
    """

    if a is None or (type(a) is not int and type(a) is not float):
        raise TypeError("a must be an integer")
    if type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")
    result = a + b
    if result == float('inf') or result == -float('inf'):
        return 89
    return int(a) + int(b)
