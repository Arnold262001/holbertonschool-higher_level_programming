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
        if isinstance(attrs, list) and all(isinstance(a, str) for a in attrs):
            return {k: v for k, v in self.__dict__.items() if k in attrs}
        return self.__dict__

    def reload_from_json(self, json):
        for k, v in json.items():
            setattr(self, k, v)
        return self
