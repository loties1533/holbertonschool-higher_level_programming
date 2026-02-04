#!/usr/bin/python3
"""
Module qui définit une fonction pour lister les attributs
et les méthodes disponibles d'un objet
"""


def lookup(obj):
    """
    Retourne la liste des attributs et méthodes disponibles d'un objet

    Args:
        obj (object): L'objet dont on veut lister les attributs et méthodes

    Returns:
        list: Liste contenant les attributs et méthodes de l'objet
    """
    return dir(obj)
