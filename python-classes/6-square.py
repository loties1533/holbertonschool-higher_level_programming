#!/usr/bin/python3
"""
classe Square qui definit un carré
selon la taille (size) et position (x,y)
"""


class Square:
    """
    reprensente un carré avec un attribut privé 'size' pour la taille
    et un deuxieme pour la 'position' du carré position avec (x et y)
    """
    def __init__(self, size=0, position=(0, 0)):
        """
        initialisation d un objet carré (square)

        args:
        size (int) taille du coté (0 par defaut)
        position (tuple) : x et y (0 et 0 par defaut)
        raise :
        TypeError si 'size' n est pas en entier
        TypeError si 'position' n est pas un tuple  de 2 entier
        ValueError si size  < 0

        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """
        recupere la taille du carré

        return : int ( taille du coté du carré )

        permet d accéder(lire) la valeur sans toucher a l attribut privé
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

    @property
    def position(self):
        """
        recupere la position du carré

        return : tuple (x, y)
        """
        return self.__position

    @position.setter
    def position(self, valeur):
        """
        modifie la position de carré

        args : valeur du tuple (2) pour la position de 'x' et 'y'

        raise :
            TypeError: si le tuple n a pas 2 entier positif en valeur
        """
        if not isinstance(valeur, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        if len(valeur) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        for nombre in valeur:
            if not isinstance(nombre, int) or nombre < 0:
                raise TypeError(
                    "position must be a tuple of 2 positive integers"
                    )
        self.__position = valeur

    def area(self):

        """
        calcule et retourne l aire du carré
        return : (int) aire du carré = (size * size)
        """
        return self.__size * self.__size

    def my_print(self):
        """
        affiche le carré de # ds la sortie (stdout)
        si size == 0 ,ligne vide
        """
        if self.__size == 0:
            print("")
            return
        for i in range(self.__position[1]):
            print("")
        for i in range(self.__size):
            espace = " " * self.__position[0]
            ligne = "#" * self.__size
            print(espace + ligne)
