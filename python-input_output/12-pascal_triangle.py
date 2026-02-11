#!/usr/bin/python3
"""
Module pour création d'un triangle de Pascal
"""


def pascal_triangle(n):
    """
    retourne le triangle sous forme de liste de ligne
    chaque ligne du triangle est une soud liste qui contient les nombres
    par rapport a sa ligne
    i = compteur / j = parcours les éléments
    """
    if n <= 0:
        return []

    triangle = []

    for i in range(n):
        ligne = [1]
        if i > 0:
            ligne_preced = triangle[-1]
            for j in range(1, i):
                ligne.append(ligne_preced[j - 1] + ligne_preced[j])
            ligne.append(1)
        triangle.append(ligne)
    return triangle
