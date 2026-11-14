#!/usr/bin/env python3
"""Demonstrate inheritance and method overriding."""


class Animal:
    """Represent an animal with a basic speaking behavior."""

    def speak(self):
        """Return the default animal sound."""
        return "Some sound"


class Dog(Animal):
    """Represent a dog with its own speaking behavior."""

    def speak(self):
        """Return the sound made by a dog."""
        return "Woof"


class Cat(Animal):
    """Represent a cat with its own speaking behavior."""

    def speak(self):
        """Return the sound made by a cat."""
        return "Meow"


animals = [Dog(), Cat(), Dog()]

for animal in animals:
    print(animal.speak())

dog = Dog()

print(isinstance(dog, Dog))
print(isinstance(dog, Animal))
print(issubclass(Dog, Animal))
