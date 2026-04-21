#!/usr/bin/python3
"""
This module contains a function that returns the dictionary
description with simple data structure.
"""


def class_to_json(obj):
    """Returns the dictionary description for JSON serialization."""
    return obj.__dict__
