#!/usr/bin/python3
"""
fonction qui verifie si l objet est une instence de class ou de sous class
"""


def is_kind_of_class(obj, a_class):
    """
    retourn 'true' si si 'obj' est une instence de 'a_class' ou sous class
    sinon retourn 'false'

    args
    - obj = l objet verifier
    - a_class = la class a comparer 
    (si c bien une instence de cette class ou sous class)

    return
        - true si obj et bien une instence de a_class ou une sous class ,
        sinon false
    """
    return isinstance(obj, a_class)
