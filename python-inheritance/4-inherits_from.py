#!/usr/bin/python3
"""
Ete módulo define la función para validar
la instancia.
"""


def inherits_from(obj, a_class):
    """
    Esta funcion verifica que el objeto sea
    una instancia de una clase o que haya
    heredado de una clase.

    Args:
        obj (object):El obejto a validar.
        a_class (class or tuple): Una clase
        o una tupla con la clases.

    Returns:
        bool (True): Caso verdadero,False caso contrario.
    #     """

    if issubclass(type(obj), a_class):
        if isinstance(obj, a_class):
            return True
    return False
