#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrice = []

    for line in matrix:
        new_line = []
        for valeur in line:
            new_line .append(valeur ** 2)
        new_matrice.append(new_line)
    return new_matrice
    