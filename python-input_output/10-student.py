#!/usr/bin/python3
"""
This module defines a Student class with filtered JSON retrieval.
"""


class Student:
    """A Student class."""

    def __init__(self, first_name, last_name, age):
        """Instantiates a Student object."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieves a dictionary representation of a Student instance."""
        if type(attrs) is list and all(type(i) is str for i in attrs):
            return {k: v for k, v in self.__dict__.items() if k in attrs}
        return self.__dict__
