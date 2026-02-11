#!/usr/bin/python3
import csv
import json

def convert_csv_to_json(csv_filename):
    try:
        with open(csv_filename, "r", encoding="utf-8") as csvfile:
            lecteur = csv.DictReader(csvfile)
            donnees = [ligne for ligne in lecteur]

        with open("data.json", "w", encoding="utf-8") as jsonfile:
            json.dump(donnees, jsonfile, indent=4)

        return True
    except FileNotFoundError:
        return False
