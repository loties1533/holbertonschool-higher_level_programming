#!/usr/bin/python3
"""
fonction qui renvoie True  si un objet est l'instance d'une class qui  herite
(directement ou indirectement) d'une class spécifique (a_class)
"""


def inherits_from(obj, a_class):
    """
    verifie si obj et une instance d'une sous class de 'a_class'
    et pas une instence directement de 'a_class'

    args
    - obj = l objet verifier
    - a_class = la class sur laquelle on verifie

    return
        - true si obj et bien une instence de sous classe a_class ,
        sinon false
    """
    return isinstance(obj, a_class) and type (obj) is not a_class
