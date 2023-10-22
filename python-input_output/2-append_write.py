#!/usr/bin/python3
"""
Este módulo define la función append_write,
"""


def append_write(filename="", text=""):
    """
    Esta función agrega contenido al final de un fichero,
    crea el archivo si no existe.

    Args:
        filename (str): Ruta al del archivo.
        text (str): Contenido a agregar al fichero
    Returns:
        int : cantidad de caracteres escritos
    """
    with open(filename, 'a', encoding='UTF-8') as fa:
        return fa.write(text)
