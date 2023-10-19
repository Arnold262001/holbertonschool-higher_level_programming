#!/usr/bin/python3
"""
Este modulo definea una clase vacia.
"""


class BaseGeometry:
    """
    Esta clase define BaseGeomatry.
    """

    def area(self):
        """
        Esta funcion lanza una Exception.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if type(value) != int:
            raise TypeError(f"{name} must be an integer")

        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
