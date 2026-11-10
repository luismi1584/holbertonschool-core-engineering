#!/usr/bin/env python3
"""Define a Square class with size, position, and string representation."""


class Square:
    """Represent a square with validated size and position."""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize a square with its size and position."""
        self.size = size
        self.position = position

    @property
    def size(self):
        """Return the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size after validating its type and value."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Return the position of the square."""
        return self.__position

    @position.setter
    def position(self, value):
        """Set the position after validating its contents."""
        if (not isinstance(value, tuple) or len(value) != 2
                or not all(isinstance(n, int) and n >= 0 for n in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Return the area of the square."""
        return self.__size ** 2

    def my_print(self):
        """Print the square using its size and position."""
        print(self)

    def __str__(self):
        """Return the square as a string using its position."""
        if self.__size == 0:
            return ""

        lines = [""] * self.__position[1]

        for i in range(self.__size):
            lines.append(" " * self.__position[0] + "#" * self.__size)

        return "\n".join(lines)
