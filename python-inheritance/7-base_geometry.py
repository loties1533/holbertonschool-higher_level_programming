#!/usr/bin/python3
"""
module BaseGeometry
Contient la classe BaseGeometry avec area et integer_validator
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

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        valide uniquement des entier positif
        sinon TypeError ou ValueError
        """

        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
