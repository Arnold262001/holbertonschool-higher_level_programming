#!/usr/bin/python3
"""
Este módulo define la función
save_to_json, para guardar en un archivo .json
"""


import json


def save_to_json_file(my_obj, filename):
    """
    Esta función serializa un objeto python y lo
    guarda en fichero.

    Args:
        my_obj (obj): Objeto a serializar.
        filename (str) : Ruta del fichero.
    """

    with open(filename, 'w') as fw:
        json.dump(my_obj, fw)
