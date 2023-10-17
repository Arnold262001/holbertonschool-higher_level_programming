#!/usr/bin/python3
"""
Este módulo define una clase que hereda de list
"""


class MyList(list):
    """
    Esta clase toma la funcionalidad heredando de list.
    """

    def print_sorted(self):
        """
        Esta función imprime una copia de la lista ordenada.
        """

        print(sorted(self))

    def __repr__(self):
        """
        Este métodod regresa un string, representación de lista.

        Returns:
            list (list): Regresa la representación de la lista.
        """

        return f"{list(self)}"
