#!/usr/bin/python3
"""
Esta módulo define la clase Student.
"""


class Student:
    """
    Esta clase define a Student.
    """

    def __init__(self, first_name, last_name, age):
        """
        Este método constructor recive 3 parámteros.

        Args:
            first_name (str): Primer nombre
            last_name (str): Apellidos
            age (int): Edad
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Esta función regresa una diccionario con los atributos
        de nuestra instancia.

        Returns:
            dict: Regresa un diccionario con los atributos
                de instancia.
        """
        if attrs:
            if all(True if type(a) == str else False for a in attrs):
                temp_dict = dict()
                for k in self.__dict__.keys():
                    if k in attrs:
                        temp_dict[k] = self.__dict__[k]
                return temp_dict
        return self.__dict__
