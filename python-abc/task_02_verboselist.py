#!/usr/bin/env python3
"""
Module verbose_list : liste avec notifications lors des modification
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

        count = len(elem_added)
        super().extend(elem_added)
        print("Extended the list with [{}] items.".format(count))

    def remove(self, element):

        super().remove(element)
        print("Removed [{}] from the list.".format(element))

    def pop(self, at_index=-1):
        element = super().pop(at_index)
        print("Popped [{}] from the list.".format(element))
        return element
