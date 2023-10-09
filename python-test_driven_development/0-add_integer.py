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
    """

    if type(a) != int and type(a) != float:
        raise TypeError("a must be an integer")

    if type(b) != int and type(b) != float:
        raise TypeError("b must be an integer")

    a = int(a) if type(a) == float else a
    b = int(b) if type(b) == float else b

    return a + b
