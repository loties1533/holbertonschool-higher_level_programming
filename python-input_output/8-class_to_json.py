#!/usr/bin/python3
"""
Module 8-class_to_json
fonction pour transformer une instance de class
en dictionnaire valide pour sérialisation JSON
"""


def class_to_json(obj):
    """
    retourn le dict des attribut d’un objet
    Args:
        obj (object) = instance de classe

    Return :
        dict =  dictionnaire avec les attribut de l'objet
    """
    return obj.__dict__
