#!/usr/bin/python3
"""Square sinfini təyin edən modul."""


class Square:
    """Kvadratı təmsil edən sinif."""

    def __init__(self, size=0):
        """Yeni Kvadrat yaradan metod (Constructor).

        Args:
            size (int): Kvadratın tərəfinin ölçüsü.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Kvadratın sahəsini hesablayan metod.

        Returns:
            Kvadratın sahəsi (size * size).
        """
        return self.__size * self.__size
