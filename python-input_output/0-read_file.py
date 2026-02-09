#!/usr/bin/python3
"""
Module qui lit un fichier et affiche son contenu : Encodage UTF-8
"""


def read_file(filename=""):
    """
    fonction qui lit et affiche contenue d un fichier
    """
    with open(filename, "r", encoding="utf-8") as fichier:
        print(fichier.read(), end="")
