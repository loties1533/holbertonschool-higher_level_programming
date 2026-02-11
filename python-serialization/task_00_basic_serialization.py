#!/usr/bin/python3
"""
task_00_basic_serialization.py
Sérialisation et désérialisation de base en Python vers/depuis des fichiers JSON.
"""

import json


def serialize_and_save_to_file(data, filename):
    """
    serialise un dictionnaire python et l enregistre dans un fichier JSON

    Args:
        data (dict) =  dictionnaire Python a serialiser
        filename (str) = nom du fichier JSON en sortie
    """
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f)

def load_and_deserialize(filename):
    """
    recup un fichier JSON et le déserialise en dict python

    Args:
        filename (str) = Nom du fichier JSON 

    Return:
        dict = dict python avec donnée déserialisé
    """
    with open(filename, "r", encoding="utf-8") as f:
        data = json.load(f)
    return data
