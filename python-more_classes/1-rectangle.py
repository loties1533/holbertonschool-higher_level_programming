#!/usr/bin/python3
"""
class rectangle avec largeur (width) et hauteur (height) privé
gerer avec getter / setter
"""


class Rectangle:
    """
    définit la class rectangle avec width et height
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
        """pour  recuperer la largeur rectangle (getter)"""
        return self.__width

    @width.setter
    def width(self, value):
        """
        pour modifié la largeur (setter) si verifications
        type / valeur est valide (un entier superieur a (0)
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """pour  recuperer la heuteur du rectangle (getter)"""
        return self.__height

    @height.setter
    def height(self, value):
        """
        pour modifié la hauteur (setter) si verifications
        type / valeur est valide (un entier superieur a 0)
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
