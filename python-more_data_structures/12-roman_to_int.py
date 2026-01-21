#!/usr/bin/python3
def roman_to_int(roman_string):
    if (roman_string is None or
            not isinstance(roman_string, str) or
            roman_string == ""):
        return 0

    valeur = {
        "I": 1, "V": 5, "X": 10, "L": 50,
        "C": 100, "D": 500, "M": 1000
    }
    total = 0

    for i in range(len(roman_string)):
        if (i + 1 < len(roman_string) and
                valeur[roman_string[i]] <
                valeur[roman_string[i + 1]]):
            total -= valeur[roman_string[i]]
        else:
            total += valeur[roman_string[i]]

    return total
