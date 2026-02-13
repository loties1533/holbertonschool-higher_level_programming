#!/usr/bin/python3
"""
sérialisation et déserialisation d un dictionnaire
Python vers un  fichier XML
"""
import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """
    serialise un dict Python et enregistre dans un fichier
    Args:
        dictionary (dict) = dictionnaire Python à sérialiser
        filename (str) = nom fichier XML en sortie
    """
    root = ET.Element("data")

    for key in dictionary:
        element = ET.SubElement(root, key)
        element.text = str(dictionary[key])
    tree = ET.ElementTree(root)
    tree.write(filename)


def deserialize_from_xml(filename):
    """
    recupere le fichier XML et le deserialise en dict Python
    Args:
        filename (str) = nom du fichier XML

    Returns:
        dict: dictionnaire Python avec donnée désérialisé
    """
    tree = ET.parse(filename)
    root = tree.getroot()

    result = {}

    for element in root:
        result[element.tag] = element.text

    return result
