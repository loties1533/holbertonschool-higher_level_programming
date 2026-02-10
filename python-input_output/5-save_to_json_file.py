#!/usr/bin/python3
"""
Module pour sauvegarder un objet python dans un fichier JSON
"""
import json


def save_to_json_file(my_obj, filename):
    """
    rentre un objet python dans un format JSON
    """
    with open(filename, "w", encoding="utf-8")as fichier:
        json.dump(my_obj, fichier)
