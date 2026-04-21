#!/usr/bin/python3
"""
This module contains a class MyList that inherits from list.
"""


class MyList(list):
    """A custom list class that inherits from Python's built-in list."""

    def print_sorted(self):
        """Prints the elements of the list in sorted (ascending) order."""
        print(sorted(self))
