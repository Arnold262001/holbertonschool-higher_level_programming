#!/usr/bin/python3
"""
Este módulo contiene operaciones matemáticas
"""


def add_integer(a, b=98):
    """
    Esta función suma dos enteros.

    Args:
        a (int): Primer entero
        b (int): Segundo entero(valor por defecto 98)
    """

    if (type(a) != int or type(a) != float) or a is None:
        raise TypeError("a must be an integer")

    if type(b) != int or type(b) != float:
        raise TypeError("b must be an integer")

    return int(a) + int(b)
