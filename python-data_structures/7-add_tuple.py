#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    premier_a = tuple_a[0] if len(tuple_a) > 0 else 0
    deuxieme_a = tuple_a[1] if len(tuple_a) > 1 else 0

    premier_b = tuple_b[0] if len(tuple_b) > 0 else 0
    deuxieme_b = tuple_b[1] if len(tuple_b) > 1 else 0

    resultat0 = premier_a + premier_b
    resultat1 = deuxieme_a + deuxieme_b

    return (resultat0, resultat1)
