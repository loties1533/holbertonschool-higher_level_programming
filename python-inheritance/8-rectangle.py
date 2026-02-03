#!/usr/bin/python3
"""
module rectangle
contient class rectangle qui hérite de basegeometry
"""

class BaseGeometry:
    """
    Class de base avec la methode de validation d entier
    """

    def integer_validator(self, name, value):
        """
        verifie que value est un entier
        """
        if type(value) != int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")

class Rectangle(BaseGeometry):
    """
    class Rectangle qui herite de basegeometry
    affiche un rectangle avec largeur / hauteur
    """

    def __init__(self, width, height):
        """
        initialisation avec width et height valide
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """
        retourne l aire du rectangle
        """
        return self.__width * self.__height

    def __str__(self):
        """
        retourne la représentation en string du rectangle
        """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
