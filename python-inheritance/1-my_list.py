#!/usr/bin/python3
"""
class MyList qui herite de list et ajout methode de trie
"""


class MyList(list):
    """
    ma class qui herité de liste et va ajouté une methode
    pour afficher une liste triée
    """
    def print_sorted(self):
        """crée une nouvelle liste par ordre croissant"""
        print(sorted(self))
