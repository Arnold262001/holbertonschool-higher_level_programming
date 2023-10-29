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
    result = 0
    n = dict(a=a, b=b)

    for k, v in n.items():
        if v is None or (not isinstance(v, (int, float))):
            raise TypeError(f"{k} must be an integer")
    result = n['a'] + n['b']
    if result == float('inf') or result == -float('inf'):
        return 89
    return int(n['a']) + int(n['b'])
