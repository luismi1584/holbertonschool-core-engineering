#!/usr/bin/env python3
"""Define a Square class with its own string representation."""

Rectangle = __import__('2-rectangle').Rectangle


class Square(Rectangle):
    """Represent a square with a positive integer size."""

    def __init__(self, size):
        """Initialize a square using its validated size."""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """Calculate and return the area of the square."""
        return self.__size * self.__size

    def __str__(self):
        """Return a readable description of the square."""
        return "[Square] {}/{}".format(self.__size, self.__size)
