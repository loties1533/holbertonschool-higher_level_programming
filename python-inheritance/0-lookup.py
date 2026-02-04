#!/usr/bin/python3
"""
fonction qui renvoie la liste des attributs et méthodes disponibles d'un objet
"""


def lookup(obj):
    """
    renvoie la liste d un objet
    args = obj
    return : liste de obj
    """
    return dir(obj)
