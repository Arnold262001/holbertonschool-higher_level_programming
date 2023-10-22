#!/usr/bin/python3
"""
Este módulo define  la función
load_from_file, para convertir string Json a objeto python.
"""
import json


def load_from_json_file(filename):
    """
    Esta función deserializa un el contenido de
    un archivo enun objeto de python.

    Args:
        filename (str): Nombre del fichero donde se encuentra
        los datos a deserializar.
    Returns:
        obj: Regresa un objeto de python.
    """
    with open(filename, 'r') as fr:
        content = fr.read()
        return json.loads(content)
