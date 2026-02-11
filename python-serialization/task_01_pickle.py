#!/usr/bin/python3
"""
sérialisation et déserialisation d une class python personnalisée
"""
import pickle


class CustomObject:
    """
    classe qui represente  un obj personnalisée avec sérialisation
    """
    def __init__(self, name, age, is_student):
        """
        initialisation de l'objet:
        name (str)
        age (int)
        is_student (bool)
        """
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """
        affiche les attribut d'un objet
        """
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        """
        sérialise l'objet et l enregistre dans fichier 'filename'
        ou renvoi : None si une erreur
        """
        try:
            with open(filename, "wb") as fichier:
                obj = pickle.dump(self, fichier)
            return obj
        except (OSError, pickle.PickleError):
            return None

    @classmethod
    def deserialize(cls, filename):
        """
        désérialise l'objet via le fichier filename
        ou renvoie : None si le fichier n'existe pas
        """
        try:
            with open(filename, "rb") as fichier:
                obj = pickle.load(fichier)
            return obj
        except (OSError, pickle.PickleError):
            return None
