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
        leve une exception car la méthode n'est pas implémentée
        """

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Valide qu'une valeur est un entier positif
        leve TypeError si ce n'est pas un entier ou ValueError si <= 0
        """

        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
