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

### 7. Print Square Instance
- File: `6-square.py`
- Defines a `Square` class with private `__size` and `__position` attributes.
- Uses `__init__(self, size=0, position=(0, 0))`.
- Implements getters and setters for size and position.
- Validates that size is a non-negative integer.
- Validates that position is a tuple of two non-negative integers.
- Raises `TypeError` for invalid position values.
- Provides an `area(self)` method.
- Implements `my_print(self)` to print the square using `#`.
- Uses position to control horizontal spaces and vertical blank lines.
- Implements `__str__(self)` to control the string representation.
- Allows `print(square)` to produce the same visual output as `square.my_print()`.

### 8. Rectangle Class
- File: `1-rectangle.py`
- Defines a `Rectangle` class with private `__width` and `__height` attributes.
- Uses `__init__(self, width=0, height=0)` to initialize the rectangle.
- Implements getters using `@property`.
- Implements setters using `@width.setter` and `@height.setter`.
- Validates that width and height are non-negative integers.
- Raises `TypeError` for invalid types.
- Raises `ValueError` for negative values.
- Uses the setters during initialization to centralize validation.
- Preserves previously valid dimensions when invalid assignments are attempted.

### 9. Area and Perimeter
- File: `2-rectangle.py`
- Extends the Rectangle class with area and perimeter methods.
- Maintains private `__width` and `__height` attributes.
- Uses properties and setters to validate rectangle dimensions.
- Implements `area(self)` to return width multiplied by height.
- Implements `perimeter(self)` to return twice the sum of width and height.
- Returns a perimeter of 0 when either width or height is 0.
- Supports updating dimensions after object creation.
- Preserves the validation behavior from the previous Rectangle class.
