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

    @property
    def size(self):
        """
        recupere la taille du carré

        return : int ( taille du coté du carré )

        permet d accéder a la valeur sans toucher a l attribut privé
        """
        return self.__size

    @size.setter
    def size(self, valeur):
        """
        modifie la taille du carré

        args : valeur (int) pour nouvelle taille du coté

        Modifie la taille du carré

        vérifie que la valeur est correcte avant de l affecter

        """
        if not isinstance(valeur, int):
            raise TypeError("size must be an integer")

        if valeur < 0:
            raise ValueError("size must be >= 0")

        self.__size = valeur

    def area(self):
        """
        calcule et retourne l aire du carré
        return : (int) aire du carré = size * size
        """
        return self.__size * self.__size
