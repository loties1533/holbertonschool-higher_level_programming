#!/usr/bin/python3
"""
Module 3-is_kind_of_class
contient une fonction qui vérifie si un objet est une instance d'une classe
ou d'une sous-classe
"""


def is_kind_of_class(obj, a_class):
    """
    Vérifie si un objet est une instance d'une classe demander
    ou d'une sous-classe

    Args:
        obj (objet): L'objet à tester
        a_class (type): La classe à vérifier

    Returns:
        bool: True si obj est une instance de a_class ou d'une sous-classe,
        sinon False
    """
    return isinstance(obj, a_class)
