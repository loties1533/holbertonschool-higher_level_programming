#!/usr/bin/python3
"""
classe Square qui definit un carré
"""


class Square:
    """
    reprensente un carré avec un attribut privé 'size' pour la taille
    """
    def __init__(self, size):
        """
        initialisation de l objet square
        appelée lors de la création d un nouvel objet
        recupere la taille de square , et la stok dans attribut privé __size
        """

        self.__size = size
