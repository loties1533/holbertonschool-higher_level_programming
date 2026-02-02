#!/usr/bin/python3
"""
fonction qui renvoie la liste des attributs et méthodes disponibles d'un objet
"""


def lookup(obj):
    """
    return : la liste d attribut et methode de class ou objet
    """
    return dir(obj)
