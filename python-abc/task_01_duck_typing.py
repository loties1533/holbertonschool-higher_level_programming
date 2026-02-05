#!/usr/bin/env python3
"""
Module pour gérer des formes géométriques avec une classe abstraite Shape.
Contient les classes Circle et Rectangle, et une fonction shape_info
pour afficher l'aire et le périmètre de n'importe quelle forme.
"""

from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """
    Classe abstraite 'Shape' pour représenter une forme géométrique.
    """

    @abstractmethod
    def area(self):
        """Calcul de l'aire (méthode abstraite)."""
        pass

    @abstractmethod
    def perimeter(self):
        """
        calcul du périmètre (méthode abstraite)
        """
        pass


class Circle(Shape):
    """
    Classe Circle (cercle) qui hérite de Shape.
    """

    def __init__(self, radius):
        """
        Initialisation du cercle avec le rayon
        """
        self.radius = abs(radius)

    def area(self):
        """
        calcul de l aire du cercle
        """
        return math.pi * self.radius ** 2

    def perimeter(self):
        """Calcul du périmètre du cercle."""
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    """
    Classe Rectangle qui hérite de Shape
    """

    def __init__(self, width, height):
        """
        Initialisation avec largeur (width) et hauteur (height)
        """
        self.width = abs(width)
        self.height = abs(height)

    def area(self):
        """
        Calcul de l'aire du rectangle
        """
        return self.width * self.height

    def perimeter(self):
        """
        Calcul du périmètre du rectangle.
        """
        return 2 * (self.width + self.height)


def shape_info(shape):
    """
    affiche l'aire et le périmetre pour toute forme
    shape_info ne vérifie pas le type de la forme
    """
    print(f"Area: {shape.area()}")
    print(f"Perimeter: {shape.perimeter()}")
