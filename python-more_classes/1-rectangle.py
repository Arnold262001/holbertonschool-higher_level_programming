#!/usr/bin/python3
"""
Este modulo define una clase
"""


class Rectangle:
    """
    Esta clase define un rectángulo
    """

    def __init__(self, width=0, height=0):
        """
        Método constructor, recibe el ancho y alto

        Args:
            width (int): Ancho del rectángulo.
            height (int): Alto del rectángulo
        """
        self.__height = height
        self.__width = width

    @property
    def width(self):
        """
        Este atributo regresa el ancho del rectángulo

        Returns:
            int: Retorna el ancho(height)
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Este atributo configura el ancho del rectángulo.

        Args:
            value (int): Este valor configura el ancho del rectágulo.
        """
        if type(value) != int:
            raise TypeError("width must be an integer")

        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        Este atributo regresa el alto del rectángulo.

        Returns:
            int: Retorna el alto(height)
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Este atributo configura el valor de __height

        Args:
            value (int): Este valor configura el alto del rectángulo.
        """
        if type(value) != int:
            raise TypeError("height must be an integer")

        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
