#!/usr/bin/env python3
"""
module qui définit la class IterateurCompteur :
permet de parcourir un itérable
tout en comptant le nombre d'élément deja parcouru
"""


class CountedIterator:
    """
    parcourt un itérable
    compteur pour nombre d'itération
    """
    def __init__(self, iterable):
        """
        initialise itérateur et compteur
        Args:
        iterable = tout objet itérable (list,tuple,chaine, etc ...)
        """
        self.it = iter(iterable)
        self.compteur = 0

    def __next__(self):
        """
        renvoie l élément suivant
        incrémentation du compteur +1
        Returns:
            élément suivant de l'itérable
        Raises:
            StopIteration: si plus aucun élément disponible
        """
        element = next(self.it)
        self.compteur += 1
        return (element)

    def get_count(self):

        return (self.compteur)
