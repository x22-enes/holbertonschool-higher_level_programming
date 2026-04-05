#!/usr/bin/python3
"""Square sinfini təyin edən modul."""


class Square:
    """Kvadratı təmsil edən sinif."""

    def __init__(self, size=0):
        """Yeni Kvadrat yaradan metod.

        Args:
            size (int): Kvadratın tərəfinin ölçüsü.
        """
        self.size = size

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

    def area(self):
        """Kvadratın sahəsini hesablayan metod."""
        return self.__size * self.__size

    def my_print(self):
        """Kvadratı '#' simvolu ilə standart çıxışa çap edən metod."""
        if self.__size == 0:
            print("")
        else:
            for i in range(self.__size):
                print("#" * self.__size)
