#!/usr/bin/python3
"""
Module qui définit une fonction pour lister les attributs
et méthode disponibles d'un objet
"""


def lookup(obj):
    """
    Retourne la liste des attribut et méthode disponibles d'un objet

    Args:
        obj (object): l objet dont on veut lister les attribut et méthode

    Returns:
        list: liste contenant les attribut et méthode de l'objet
    """
    return dir(obj)
