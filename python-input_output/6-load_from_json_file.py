#!/usr/bin/python3
"""
Module  qui crée un objet à partir d'un "fichier JSON"
"""

import json


def load_from_json_file(filename):
    """
    lit un fichier JSON et retourn obj python qui correspond
    """
    with open(filename, "r", encoding="utf-8") as fichier:
        return json.load(fichier)
