#!/usr/bin/python3
"""
Este módulo define una clase
"""


class LockedClass:
    """
    Esta clase define a LockedClass
    """

    __slots__ = ['first_name']

    def __setattr__(self, name, value):
        """
        Este metodo mágico sirve para crear un atributo especifico de
        forma dinámica y lanza un error de no serlo.
        """

        if name != 'first_name':
            raise AttributeError(
                f"'LockedClass' object has no attribute '{name}'")

        super().__setattr__(name, value)
