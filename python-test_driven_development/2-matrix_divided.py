#!/usr/bin/python3
"""
module 2-matrix_divided
fonction qui divise tous les éléments d'une matrice
chaque élément doit être un entier ou un float
"""


def matrix_divided(matrix, div):

    """
    divise tous les éléments d'une matrice par div, arrondis à 2 décimales
    """

    if not isinstance(matrix, list) or len(matrix) == 0:
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats"
            )
    for ligne in matrix:
        if not isinstance(ligne, list):
            raise TypeError(
                "matrix must be a matrix (list of lists) of integers/floats"
                )
    lon_ligne = len(matrix[0])
    for ligne in matrix:
        if len(ligne) != lon_ligne:
            raise TypeError(
                "Each row of the matrix must have the same size"
                )
        for element in ligne:
            if not isinstance(element, (int, float)):
                raise TypeError(
                 "matrix must be a matrix (list of lists) of integers/floats"
                )
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    nouvelle_matrix = []
    for ligne in matrix:
        nvl_ligne = []
        for element in ligne:
            nvl_ligne.append(round(element / div, 2))
        nouvelle_matrix.append(nvl_ligne)

    return nouvelle_matrix
