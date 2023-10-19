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
        """
        Este método valida si el parametro value es un int.

        Args:
            name (str): Nombre de parametro value
            value (int): Valor a evaluar.

        Raises:
            TypeError value != int
            ValueError value <= 0

        Returns:
            None
        """
        if type(value) != int:
            raise TypeError(f"{name} must be an integer")

        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")


class Rectangle(BaseGeometry):
    """
    Esta clase define un Rectangle
    """

    def __init__(self, width, height):
        """
        Este metodo inicializa con el ancho y alto del rectangulo

        Args:
            width (int): Ancho del rectangulo.
            height (int): Alto del rectangulo.
        """

        self.__width = width
        self.__height = height
