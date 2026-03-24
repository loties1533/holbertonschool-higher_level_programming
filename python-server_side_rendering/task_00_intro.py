#!/usr/bin/python3
"""
Générateur d'invitations personnalisées.
Ce script lit un template et une liste d'invités pour créer
des fichiers texte individuels numérotés.
"""
import os


def generate_invitations(template, attendees):
    # Vérification du type de template
    if not isinstance(template, str):
        print("Error: template must be a string.")
        return

    # Correction de l'indentation ici (bien aligné avec le if du dessus)
    if (not isinstance(attendees, list) or
            not all(isinstance(a, dict) for a in attendees)):
        print("Error: attendees must be a list of dictionaries.")
        return

    # Vérification du contenu vide
    if not template:
        print("Template is empty, no output files generated.")
        return
    if not attendees:
        print("No data provided, no output files generated.")
        return

    # Boucle sur les invités
    for i, attendee in enumerate(attendees, start=1):
        content = template
        placeholders = ["name", "event_title", "event_date", "event_location"]

        for j in placeholders:
            valeur = attendee.get(j)
            if valeur is None:
                valeur = "N/A"
            # Remplacement des {balises} par les valeurs
            content = content.replace(f"{{{j}}}", str(valeur))

        filename = f"output_{i}.txt"

        # Vérification d'existence (Hint os.path.exists)
        if os.path.exists(filename):
            pass

        # Écriture sécurisée
        try:
            with open(filename, 'w') as f:
                f.write(content)
        except Exception as e:
            print(f"Error {filename}: {e}")
