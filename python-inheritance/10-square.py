#!/usr/bin/python3
"""
This module defines a Square class that inherits from Rectangle.
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """A Square class that inherits from Rectangle."""

    def __init__(self, size):
        """Instantiates a Square with a validated size."""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)
