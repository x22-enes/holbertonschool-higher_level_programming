#!/usr/bin/python3
"""Square sinfini təyin edən modul."""


class Square:
    """Kvadratı təmsil edən sinif."""

    def __init__(self, size=0, position=(0, 0)):
        """Yeni Kvadrat yaradan metod.

        Args:
            size (int): Kvadratın ölçüsü.
            position (tuple): Kvadratın (x, y) koordinatları.
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Ölçünü əldə etmək üçün getter."""
        return self.__size

    @size.setter
    def size(self, value):
        """Ölçünü təyin etmək üçün setter."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Koordinatları əldə etmək üçün getter."""
        return self.__position

    @position.setter
    def position(self, value):
        """Koordinatları təyin etmək üçün setter."""
        if (not isinstance(value, tuple) or len(value) != 2 or
                not all(isinstance(i, int) for i in value) or
                not all(i >= 0 for i in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Sahəni hesablayan metod."""
        return self.__size * self.__size

    def my_print(self):
        """Kvadratı '#' və koordinat boşluqları ilə çap edir."""
        if self.__size == 0:
            print("")
            return

        # Y oxu (Yuxarıdan aşağı boş sətirlər)
        [print("") for i in range(self.__position[1])]

        # X oxu (Soldan sağa boşluqlar və kvadratın özü)
        for i in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)
