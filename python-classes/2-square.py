#!/usr/bin/python3
"""
classe Square qui definit un carré
"""


class Square:
    """
    reprensente un carré avec un attribut privé 'size' pour la taille
    size vaut 0 par defaut
    """
    def __init__(self, size=0):
        """
        initialisation de l objet square
        appelée lors de la création d un nouvel objet
        size facultatif vaut 0 par dafaut
        verifie si size est un entier est vaut =< 0

        raise :
        TypeError si size n est pas en entier
        ValueError si size  < 0

        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")

        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size
