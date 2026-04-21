#!/usr/bin/python3
"""
This module defines a Square class with custom string representation.
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """A Square class that inherits from Rectangle."""

    def __init__(self, size):
        """Instantiates a Square with a validated size."""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def __str__(self):
        """Returns the string representation of the square."""
        return f"[Square] {self.__size}/{self.__size}"
