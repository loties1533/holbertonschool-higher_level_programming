#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = []
    for nb in my_list:
        if nb == search:
            new_list.append(replace)
        else:
            new_list.append(nb)

    return new_list
