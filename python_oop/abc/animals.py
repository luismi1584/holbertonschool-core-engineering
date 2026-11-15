#!/usr/bin/env python3
"""Define an abstract Animal class and its concrete subclasses."""

from abc import ABC, abstractmethod


class Animal(ABC):
    """Represent an animal with a required sound method."""

    @abstractmethod
    def sound(self):
        """Define the sound that each animal must implement."""
        pass


class Dog(Animal):
    """Represent a dog that makes a barking sound."""

    def sound(self):
        """Return the sound made by a dog."""
        return "Bark"


class Cat(Animal):
    """Represent a cat that makes a meowing sound."""

    def sound(self):
        """Return the sound made by a cat."""
        return "Meow"
