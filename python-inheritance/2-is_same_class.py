#!/usr/bin/python3
"""
Este módulo contiene la función para validar instancias.
"""


def is_same_class(obj, a_class):
    """
    Esta función verifica si un objeto perteneca a una clase.

    Args:
        obj (objeto): El objeto que se desea validar.

    Returns:
        True (bool): Sí obj pertenece a a_class, caso contrario False
    """
    return type(obj) == a_class
