#!/usr/bin/python3
"""
Module qui convertit une chaine Json
"""
import json


def from_json_string(my_str):
    """
    retoune un objet python a parir d une chaine JSON
    """
    return json.loads(my_str)
