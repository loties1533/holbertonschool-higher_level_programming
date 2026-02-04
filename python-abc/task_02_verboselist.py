#!/usr/bin/env python3
"""
Module verbose_list
Ce module définit la classe VerboseList  qui hérite de classe intégrée 'list'
cette classe ajoute un comportement personnalisé pour notifié chaque fois qu'un
élément est ajoutée ou retiré de liste , les méthode 'append'/'extend'/remove'
et 'pop' sont redéfinie pour afficher un msg exact tout en conservant
leur fonction originale
"""


class VerboseList(list):
    """
    classe verbose_list qui hérite de 'list'
    et ajoute des notifications si ajout ou suppression d'élément
    """
    def append(self, element):
        """
        ajoute un element a la liste + notification
            Args:
        element: element à ajouter à la liste
        """
        super().append(element)
        print("Added [{}] to the list.".format(element))

    def extend(self, elem_added):
        """
        ajoute plusieur élément a la liste et affiche une notif

        Args:
            element: Liste des éléments a ajouter

        count = len(elem_added)
        super().extend(elem_added)
        print("Extended the list with [{}] items.".format(count))
        """

    def remove(self, element):
        """
        Supprime un élément de la liste et affiche une notif

        Args:
            element: L'élément a supprimer de la liste
        """

        super().remove(element)
        print("Removed [{}] from the list.".format(element))

    def pop(self, at_index=-1):
        """
        Retire un élément par index et affiche une notif

        Args:
            at_index: ind de l'élément à retirer (par défaut le dernier "=-1")

        Returns:
            l'élément retiré de la liste
        """
        element = super().pop(at_index)
        print("Popped [{}] from the list.".format(element))
        return element
