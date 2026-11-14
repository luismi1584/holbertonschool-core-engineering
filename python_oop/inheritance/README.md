# Python - Inheritance & Polymorphism

This project explores inheritance, method overriding,
polymorphism, and class relationships in Python.

## Learning Objectives

- Understand parent and child classes.
- Reuse inherited methods and attributes.
- Override methods in subclasses.
- Demonstrate polymorphism.
- Use isinstance() and issubclass().

## Task 0: Introduction to Inheritance and Polymorphism

File: 0-polymorphism_demo.py

This program defines three classes:

- Animal: Parent class with a speak() method.
- Dog: Child class that overrides speak() to return "Woof".
- Cat: Child class that overrides speak() to return "Meow".

The program demonstrates polymorphism by calling speak()
on different animal objects.

It also demonstrates class relationships using isinstance()
and issubclass().

## Usage

Run the program:

    python3 0-polymorphism_demo.py

## Expected Output

    Woof
    Meow
    Woof
    True
    True
    True

## Task 1: Base Geometry

File: base_geometry.py

This program introduces the BaseGeometry class, which provides
shared functionality for geometric shapes.

### Methods

- area(self):
  Raises an Exception with the message
  "area() is not implemented".

- integer_validator(self, name, value):
  Validates that a value is a positive integer.

  Raises TypeError if the value is not an integer.
  Raises ValueError if the value is less than or equal to zero.

### Concepts

- Base classes
- Shared methods
- Input validation
- Exception handling
- Inheritance and code reuse
