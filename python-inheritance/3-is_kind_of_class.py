#!/usr/bin/python3
"""
This module contains a function that returns True if the object is an
instance of, or if the object is an instance of a class that inherited from.
"""


def is_kind_of_class(obj, a_class):
    """Returns True if obj is an instance or inherited from a_class."""
    return isinstance(obj, a_class)
