#!/usr/bin/python3
"""
Este módulo define una función para leer un archivo.
"""


def read_file(filename=""):
    """
    Esta función lee un archivo e imprime el contenido en stdout.
    """
    with open(filename) as f:
        content = f.read()
    print(content, end='')
