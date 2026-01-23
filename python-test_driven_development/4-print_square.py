#!/usr/bin/python3
"""
module 4-print_square :
affiche un carré de char #
"""


def print_square(size):
    """
    affiche un carré de # taille 'size'
    'size et obligatoirement un entier ou supereir a 0
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for _ in range(size):
        print("#" * size)
