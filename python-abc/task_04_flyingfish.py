#!/usr/bin/env python3
"""
Ce module illustre l'héritage multiple en Python
avec les classes Fish, Bird et FlyingFish.
"""


class Fish:
    """
    Classe Fish
    """

    def swim(self):
        print("The fish is swimming")

    def habitat(self):
        print("The fish lives in water")


class Bird:
    """
    Classe Bird
    """

    def fly(self):
        print("The bird is flying")

    def habitat(self):
        print("The bird lives in the sky")


class FlyingFish(Fish, Bird):
    """
    Classe FlyingFish qui hérite de Fish et Bird
    """

    def fly(self):
        print("The flying fish is soaring!")

    def swim(self):
        print("The flying fish is swimming!")

    def habitat(self):
        print("The flying fish lives both in water and the sky!")
