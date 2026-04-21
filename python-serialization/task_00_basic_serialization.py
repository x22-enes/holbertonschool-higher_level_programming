#!/usr/bin/python3
"""
This module provides basic serialization and deserialization
functionality to save and load Python dictionaries to/from JSON files.
"""
import json


def serialize_and_save_to_file(data, filename):
    """Serializes a Python dictionary to a JSON file."""
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f)


def load_and_deserialize(filename):
    """Loads and deserializes data from a JSON file."""
    with open(filename, 'r', encoding='utf-8') as f:
        return json.load(f)
