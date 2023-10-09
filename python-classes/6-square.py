#!/usr/bin/python3
"""
Este módulo representa la clase Square
"""


class Square:
    """
    Esta clase define un cuadrado
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Este es el constructor de la clase Square.
        Inicializa un nuevo objeto Square con el size recibido.

        Args:
            size (int o float): La longitud de los lados del square.
            position (tuple): Las coordenadas de impresión del cuadrado.
        """

        if type(position[0]) != int or type(position[1]) != int or len(position) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = position

        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """
        Este método retorna el área de un cuadrado.

        Returns:
            _size ** 2 (el tamaño al cuadrado)
        """
        return self.__size ** 2

    def my_print(self):
        """
        Este método imprime un cuadrado en stdout usando #,
        siempre y cuando __size > 0.
        """
        if self.__size == 0:
            print()
        else:
            for o in range(self.__position[1]):
                print()
            for i in range(self.__size):
                print("{0}{1}".format(
                    '_' * self.__position[0], '#' * self.__size))

    @property
    def size(self):
        """Esta propiedad devuelve el __size

            Returns:
                retorna el __size.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Esta función configura el valor de __size
        """
        if type(value) != int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        """
        Esta propiedad devuelve las coordenadas.

            Returns:
                retorna los puntos donde se imprimirá
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Esta función configura el valor de __position
        """
        if type(value[0]) != int or type(value[1]) != int or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value
