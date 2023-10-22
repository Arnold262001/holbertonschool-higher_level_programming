#!/usr/bin/python3
"""
Este módulo define la función
to_json_string para serializar un objeto
"""
import json


def to_json_string(my_obj):
    """
    Serializa un objeto de python a formato JSON.

    Args:
        objeto (obj): Objeto python a serializar

    Returns:
        str: Regresa un string en formato JSON.
    """
    return json.dumps(my_obj)
