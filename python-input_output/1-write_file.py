#!/usr/bin/python3
"""
Module pour ecrire du texte dans un fichier
"""


def write_file(filename="", text=""):
    """
    ecrit du text dans un fichier .txt et retourne le nombres de caracteres
    """
    with open(filename, "w", encoding="utf-8") as fichier:
        return fichier.write(text)
