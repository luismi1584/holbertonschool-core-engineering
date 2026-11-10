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

### 4. Area of a Square
- File: `3-square.py`
- Defines a `Square` class with a private `__size` attribute.
- Uses `__init__(self, size=0)` to initialize the square.
- Validates that the size is a non-negative integer.
- Raises `TypeError` for invalid types.
- Raises `ValueError` for negative values.
- Implements an instance method `area(self)`.
- Returns the square's area using `self.__size ** 2`.
- Preserves encapsulation through Python's name-mangling mechanism.

### 5. Access and Update Private Attribute
- File: `4-square.py`
- Defines a `Square` class with a private `__size` attribute.
- Uses `__init__(self, size=0)` to initialize the square.
- Implements a getter using `@property`.
- Implements a setter using `@size.setter`.
- Validates that size is a non-negative integer.
- Raises `TypeError` for invalid types.
- Raises `ValueError` for negative values.
- Uses `self.size = size` in the constructor to centralize validation.
- Provides an `area(self)` method to calculate the square's area.
- Preserves the previous valid size when an invalid assignment is attempted.

### 6. Printing a Square
- File: `5-square.py`
- Defines a `Square` class with a private `__size` attribute.
- Implements a getter using `@property`.
- Implements a setter using `@size.setter`.
- Validates that size is a non-negative integer.
- Provides an `area(self)` method to calculate the square's area.
- Adds a public instance method `my_print(self)`.
- Prints the square using the `#` character.
- Prints one empty line when the size is `0`.
- Supports changing the square's size through the validated setter.
