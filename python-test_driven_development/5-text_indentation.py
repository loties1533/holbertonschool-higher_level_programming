#!/usr/bin/python3
""" fonction de formatage de texte """


def text_indentation(text):
    """affiche texte avec 2 saut de ligne apres ., ? :"""
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    i = 0
    while i < len(text):
        print(text[i], end="")
        if text[i] in ".?:":
            print("\n")
            i += 1
            while i < len(text) and text[i] == " ":
                i += 1
            continue
        i += 1
