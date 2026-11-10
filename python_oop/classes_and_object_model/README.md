# Python - Classes & Object Model

This module introduces object-oriented programming (OOP) in Python,
including classes, instances, attributes, methods, and encapsulation.

## Learning Objectives

- Understand the difference between classes and instances.
- Create Python classes and objects.
- Define instance attributes and methods.
- Understand object identity and behavior.
- Implement encapsulation and input validation.
- Use special methods for object representation.

## Tasks

### 0. Exploring Objects
- Explored Python objects using the interactive interpreter.
- Used `type()` to inspect object classes.
- Used `id()` to compare object identities.
- Used `dir()` to explore available methods.
- Compared object equality (`==`) and identity (`is`).

### 1. My First Square
- File: `0-square.py`
- Created an empty class named `Square`.
- Added module and class documentation.
- Verified that instances have an empty attribute dictionary.

### 2. Square with Size
- File: `1-square.py`
- Defines a `Square` class with a private instance attribute `__size`.
- Uses `__init__(self, size)` to initialize the square.
- Demonstrates encapsulation through Python's name-mangling mechanism.
- Direct access to `size` and `__size` raises `AttributeError`.

### 3. Size Validation
- File: `2-square.py`
- Defines a `Square` class with a private `__size` attribute.
- Uses `__init__(self, size=0)` to initialize the square.
- Validates that `size` is an integer.
- Raises `TypeError` with the message `size must be an integer` for invalid types.
- Raises `ValueError` with the message `size must be >= 0` for negative values.
- Defaults to a size of `0` when no argument is provided.
