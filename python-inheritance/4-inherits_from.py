#!/usr/bin/python3
"""
This module contains a function that returns True if the object is an instance
of a class that inherited (directly or indirectly) from the specified class.
"""


def inherits_from(obj, a_class):
    """Returns True if obj is a subclass of a_class, but not the exact class."""
    return issubclass(type(obj), a_class) and type(obj) is not a_class
