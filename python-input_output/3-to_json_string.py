#!/usr/bin/python3
"""
Module pour convertir  objet Python en chaîne json
"""


import json


def to_json_string(my_obj):
    """
    retourne la representation JSON d un objet Python
    my_obj = liste, dict, etc
    """
    return json.dumps(my_obj)
