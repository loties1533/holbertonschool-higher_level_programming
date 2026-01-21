#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None or a_dictionary == {}:
        return None
    max_cle = list(a_dictionary)[0]
    max_valeur = a_dictionary[max_cle]

    for cle in a_dictionary:
        if a_dictionary[cle] > max_valeur:
            max_valeur = a_dictionary[cle]
            max_cle = cle
    return max_cle
