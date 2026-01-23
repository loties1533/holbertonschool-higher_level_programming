#!/usr/bin/python3
"""
Module 0-add_integer
Definit la fonction add_integer(a, b=98) qui additionne deux nombres
en float ou int conertit en entier
"""


def add_integer(a, b=98):
    """
    Additionne deux entiers ou floats convertis en int.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
