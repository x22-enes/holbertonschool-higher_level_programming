#!/usr/bin/python3
"""
This module provides functions to serialize a Python dictionary
into an XML format and deserialize an XML file back into a dictionary.
"""
import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """
    Serializes a Python dictionary to an XML file.

    Args:
        dictionary (dict): The dictionary to serialize.
        filename (str): The filename of the output XML file.
    """
    root = ET.Element("data")
    
    for key, value in dictionary.items():
        child = ET.SubElement(root, key)
        child.text = str(value)
        
    tree = ET.ElementTree(root)
    tree.write(filename, encoding='utf-8', xml_declaration=True)


def deserialize_from_xml(filename):
    """
    Deserializes an XML file into a Python dictionary.

    Args:
        filename (str): The filename of the input XML file.

    Returns:
        dict: The deserialized Python dictionary.
    """
    try:
        tree = ET.parse(filename)
        root = tree.getroot()
        
        result_dict = {}
        for child in root:
            result_dict[child.tag] = child.text
            
        return result_dict
    except Exception:
        return None
