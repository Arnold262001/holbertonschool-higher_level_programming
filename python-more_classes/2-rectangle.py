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
        if not isinstance(value, int):
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
        if not isinstance(value, int):
            raise TypeError("height must be an integer")

        if value < 0:
            raise ValueError("height must be >= 0")

        self.__height = value

    def area(self):
        """
        Este método cálcula el área del rectángulo

        Returns:
            int: alto * ancho
        """
        return self.__height * self.__width

    def perimeter(self):
        """
        Este método cálcula el perímetro del rectángulo.
        Sí el ancho o alto es 0, se retornará 0

        Returns:
            int: alto * 2 + ancho * 2
        """
        if self.__height == 0 or self.__width == 0:
            return 0
        return self.__height * 2 + self.__width * 2
