#!/usr/bin/env python3
"""Define the BaseGeometry class for geometric shapes."""


class BaseGeometry:
    """Provide shared behavior for geometric shapes."""

    def area(self):
        """Raise an exception for an unimplemented area method."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate that a value is a positive integer."""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))

        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
