# Python - Abstract Classes & Interfaces

This module explores abstract base classes, abstract methods,
interfaces, duck typing, multiple inheritance, and mixins.

## Task 0: Abstract Animal Class and Its Subclasses

File: `animals.py`

### Description

Defines an abstract Animal class using Python's abc module.

The Animal class declares an abstract method named sound().
Concrete subclasses must implement this method.

### Classes

- Animal: Abstract base class defining the sound() contract.
- Dog: Implements sound() and returns "Bark".
- Cat: Implements sound() and returns "Meow".

### Example

    from animals import Animal, Dog, Cat

    dog = Dog()
    cat = Cat()

    print(dog.sound())
    print(cat.sound())

Expected output:

    Bark
    Meow

Attempting to instantiate Animal directly raises a TypeError.

### Concepts

- Abstract Base Classes (ABC)
- Abstract methods
- Inheritance
- Method overriding
- Interface-like design
