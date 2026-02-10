#!/usr/bin/python3
"""
Module qui definit une classe Student représente un étudiant avec ses
attribut public et methode pour retourner sa représentation sous forme de dict
"""


class Student:
    """
    classe qui represente un étudiant

    Args:
            first_name (str) = prénom
            last_name (str) = nom de famille
            age (int) = age
        """
    def __init__(self, first_name, last_name, age):

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):

        return self.__dict__
