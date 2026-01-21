#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None
    valeur_max = my_list[0]

    for num in my_list:
        if num > valeur_max:
            valeur_max = num
    return valeur_max
