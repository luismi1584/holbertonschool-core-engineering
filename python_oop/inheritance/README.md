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
