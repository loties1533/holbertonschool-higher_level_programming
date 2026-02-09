#!/usr/bin/python3
"""
Module pour ajouter du texte a la suite d un fichier
"""


def append_write(filename="", text=""):
    """
    ajoute du texte a la suite d un fichier
    retourne le nombres de caracteres ajouter
    """
    with open(filename, "a", encoding="utf-8") as fichier:
        return fichier.write(text)
