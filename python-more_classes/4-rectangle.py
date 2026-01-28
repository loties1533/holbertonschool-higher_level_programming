#!/usr/bin/python3
"""
class rectangle avec largeur (width) et hauteur (height) privé
gerer avec getter / setter
"""


class Rectangle:
    """
    definit la class rectangle avec width et height
    """
    def __init__(self, width=0, height=0):
        """
        créé le rectangle pour definir largeur / hauteur
        sinon valeurs par defaut (0,0)
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """pour  recuperer la largeur rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """
        pour modifié la largeur si verifications
        type / valeur est valide (un entier superieur a (0)
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """pour  recuperer la hauteur du rectangle """
        return self.__height

    @height.setter
    def height(self, value):
        """
        pour modifié la hauteur si verifications
        type / valeur est valide (un entier superieur a 0)
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        calcule l aire du rectangle
        return : aire du rectangle
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        calcule le perimetre du rectangle
        return : le perimetre ou 0 si taille / hauteur = 0
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """
        retourne un affichage du rectangle en '#'
        """
        if self.__width == 0 or self.__height == 0:
            return ""

        resultat = ""
        for i in range(self.__height):
            resultat += "#" * self.__width
            if i != self.__height - 1:
                resultat += "\n"
        return resultat

    def __repr__(self):
        """
        représentation du rectangle
        return : renvoie une representation sous forme de chaine  de l objet
        """
        return f"Rectangle({self.__width}, {self.__height})"
