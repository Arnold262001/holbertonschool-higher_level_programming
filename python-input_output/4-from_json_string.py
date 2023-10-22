#!/usr/bin/python3
"""
Ese módulo defina la función
from_json_string para deserealizar una cadena.
"""


import json


def from_json_string(my_str):
    """
    Esta función deserealiza una cadena a
    un objeto en python.

    Args:
        my_str (str): Cadena de texto a deserealizar.

    Returns:
        obj: Regresa un objeto python.
    """
    return json.loads(my_str)
