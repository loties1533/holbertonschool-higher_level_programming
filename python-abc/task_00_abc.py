#!/usr/bin/env python3

"""
definit une class abstraite de "Animal" avec 
sous class "Dog" et "Cat"
"""

from abc import ABC, abstractmethod

class Animal(ABC):
    """
    class abstraite pour animal 
    """
    @abstractmethod
    def sound(self):
        """
        methode qui doit etre donné dans chaque sous class
        ( elle va servir pour implementer le sont que renvoie chaque animaux)
         dog = "Bark"
         cat = "Meow"
         """
        pass

class Dog(Animal):
    """
    sous class de animal pour un chien (Dog)
    """
    def sound(self):
        """
        retourn le son produit par chien
        """
        return "Bark"

class Cat(Animal):
    """
    sous class animal pour un chat (Cat)
    """
    def sound(self):
        """
        retourne le son produit par chat
        """
        return "Meow"
