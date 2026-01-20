#!/usr/bin/python3
def uniq_add(my_list=[]):
    nombre_unique = set(my_list)
    total = 0
    for nb in nombre_unique:
        total += nb
    return total
