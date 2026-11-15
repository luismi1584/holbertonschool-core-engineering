#!/usr/bin/env python3
"""Demonstrate mixins using a dragon with multiple abilities."""


class SwimMixin:
    """Provide swimming behavior to other classes."""

    def swim(self):
        """Print the creature's swimming behavior."""
        print("The creature swims!")


class FlyMixin:
    """Provide flying behavior to other classes."""

    def fly(self):
        """Print the creature's flying behavior."""
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """Represent a dragon that can swim, fly, and roar."""

    def roar(self):
        """Print the dragon's roaring behavior."""
        print("The dragon roars!")
