#!/usr/bin/python3
"""
fonction qui verifie de quelle instence de class est un objet
"""


def is_same_class(obj, a_class):
    """
    retourn true si l objet est bien une instence de class

    args
        - obj = l objet verifier
        - a_class = la class a comparer (si c bien une instence de cette class)

    return
        - true si obj et bien une instence de a_class , sinon false
    """
    return type(obj) is a_class
