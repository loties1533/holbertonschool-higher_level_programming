#!/usr/bin/python3
"""
Module MyList : classe qui hérite de 'list' et ajoute une méthode pour afficher
la liste triée sans modifier l'ordre original
"""


class MyList(list):
    """
    classe MyList qui hérite des listes
    ajout la méthode print_sorted() pour afficher liste triée
    """
    def print_sorted(self):
        """
        affiche les éléments de la liste par ordre croissant
        sans toucher la liste originale
        """
        print(sorted(self))
