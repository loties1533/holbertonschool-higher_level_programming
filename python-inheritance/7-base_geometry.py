#!/usr/bin/python3
"""
Module geometry
contient la classe BaseGeometry (vide)
"""


class BaseGeometry:
    """
    classe baseGeometry : pour calculer une base geometrique 
    """
    

    def area(self):

        """
        methode pour lever une exeption car rien 
        d'implementer
        """

        raise Exception("area()is not implemented")

    def integer_validator(self, name, value):
        """
        valide uniquement des entier positif
        sinon TypeError ou ValueError
        """

        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")