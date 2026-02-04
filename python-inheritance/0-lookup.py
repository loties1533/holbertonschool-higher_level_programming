#!/usr/bin/python3
"""
module qui definit une fonction pour lister les attribut et methode dispo d'un objet
"""


def lookup(obj):
    """
    renvoie la liste d un objet
    args = obj
    return : liste de obj
    """
    return dir(obj)
