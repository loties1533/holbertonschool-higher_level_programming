#!/usr/bin/python3
"""
Module qui définit la classe Student
cette classe représente un étudiant avec ses attribut public
et des méthode pour  sérialisation et désérialisation
"""


class Student:
    """
    Classe qui représente un étudiant  avec ses attribut public

    Args:
        first_name (str): prénom
        last_name (str): nom de famille
        age (int): âge
    """

    def __init__(self, first_name, last_name, age):
        """
        Initialise un nouvel étudiant
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        retourne un dictionnaire qui reprend l'instance Student

        si attrs est une liste de chaines , les attribut
        presents dans cette liste sont inclus dans le dictionnaire retourné
        Sinon, tous les attribut sont retourné
        """
        if isinstance(attrs, list) and all(isinstance(a, str) for a in attrs):
            result = {}
            for key in attrs:
                if key in self.__dict__:
                    result[key] = self.__dict__[key]
            return result

        return self.__dict__

    def reload_from_json(self, json):
        """
        remplace les attribut d'instance
        par ceux qui sont  dans le dictionnaire JSON
        """
        for key, value in json.items():
            setattr(self, key, value)
