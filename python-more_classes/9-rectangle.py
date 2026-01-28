#!/usr/bin/python3
"""
class rectangle avec largeur (width) et hauteur (height) privé
gerer avec getter / setter
"""


class Rectangle:
    """
    represente un rectangle

    attribut d instance (privé)
        width = largeur
        height = hauteur
    attribut de class :
        number of instances = le nombre d instance de rectangle
            increment pour chaque création et decremente a chaque delette
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """
        créé le rectangle pour definir largeur / hauteur
        sinon valeurs par defaut (0,0)
        """
        self.width = width
        self.height = height

        Rectangle.number_of_instances += 1

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
        return la representation de l objet (rectangle) en chaine de caractere
        - rectangle  afficher en utilisant le symbol definit dans print_symbol
        - si largeur ou hauteur = 0 retourn une chaine vide
        """
        if self.__width == 0 or self.__height == 0:
            return ""

        symbol = (getattr(self, "print_symbol", Rectangle.print_symbol))
        if not isinstance(symbol, str):
            symbol = str(symbol)
        resultat = ""
        for i in range(self.__height):
            resultat += symbol * self.__width
            if i != self.__height - 1:
                resultat += "\n"
        return resultat

    def __repr__(self):
        """
        représentation du rectangle
        return : renvoie une representation sous forme de chaine (de l objet)
        """
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """
        message qui apparait quand on supprime l instance (ici rectangle)
        """
        print("Bye rectangle...")

        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        compare et retourne l air du plus grand rectangle (area = calcul aire )
        - si meme valeur retourne rect_1
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangl")
        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2


    @classmethod
    def square(cls, size=0):
        return cls(size, size)
