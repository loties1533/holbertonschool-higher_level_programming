#!/usr/bin/env python3
"""
Module pour gérer des forme géometrique avec une class abstraite Shape
contient les class Circle et Rectangle, et d'une fonction shape_info
pour afficher l aire et le périmetre de n'importe quelle forme
"""

from abc import ABC, abstractmethod
import math

class Shape(ABC):
    """
    class abstraite 'Shape' pour representer une forme 
    geometrique
    """

    @abstractmethod
    def area(self):
        """
        calcul de l aire 
        methode abstraite
        """

        pass
    @abstractmethod
    def perimeter(self):
        """
        calcul le perimetre
        methode abstraite
        """

        pass

class Circle(Shape):
    """
    class circle (un cercle) qui herite de shape
    """

    def __init__(self, radius):
        """
        initialisation le cercle avec le rayon 
        pour calcul du cercle
        """

        self.radius = (abs)radius

    def area(self):
        """
        calcul l aire du cercle
        """

        return math.pi * self.radius ** 2

    def perimeter(self):
        """
        calcul le perimetre du cercle
        """

        return 2 * math.pi * self.radius

class Rectangle(Shape):
    """
    class rectangle qui herite ossi de shape
    """


    def __init__(self, width, height):
        """
        initialisation avec widht et height 
        (largeur /hauteur)
        """
        self.width = width
        self.height = height

    def area(self):
        """
        calcul l air du rectangle
        """
        return self.width * self.height

    def perimeter(self):
        """
        calcul le perimentre du rectangle
        """

        return 2 * (self.width + self.height)

def shape_info(shape):
    """
    affiche et + perimetre de nomporte quelle forme 
    (shape_info ne vérifie jamais le type)
    """

    print(f"Area: {shape.area()}")
    print(f"Perimeter: {shape.perimeter()}")





