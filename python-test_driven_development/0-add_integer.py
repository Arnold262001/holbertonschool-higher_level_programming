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

    if type(a) != int and type(a) != float or a is None:
        raise TypeError("a must be an integer")

    if type(b) != int and type(b) != float or b is None:
        raise TypeError("b must be an integer")

    return int(a) + int(b)
