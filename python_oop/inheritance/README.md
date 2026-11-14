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

## Task 2: Rectangle

File: 1-rectangle.py

This program defines a Rectangle class that inherits
from BaseGeometry.

### Features

- Initializes a rectangle using width and height.
- Validates both dimensions using the inherited
  integer_validator() method.
- Stores width and height as private attributes.
- Does not provide public getters or setters.

### Validation

- TypeError is raised if a dimension is not an integer.
- ValueError is raised if a dimension is less than or
  equal to zero.

### Concepts

- Class inheritance
- Encapsulation
- Private attributes
- Method reuse
- Input validation

## Task 3: Full Rectangle

File: 2-rectangle.py

This program extends the Rectangle class by implementing
area calculation and a readable string representation.

### Features

- Inherits from BaseGeometry.
- Validates width and height using integer_validator().
- Stores dimensions as private attributes.
- Implements area() to calculate width multiplied by height.
- Implements __str__() to display the rectangle.

### Example

    r = Rectangle(3, 5)
    print(r)
    print(r.area())

Expected output:

    [Rectangle] 3/5
    15

### Concepts

- Inheritance
- Method overriding
- Polymorphism
- Encapsulation
- String representation using __str__()

## Task 4: Square #1

File: 1-square.py

This program defines a Square class that inherits from Rectangle.

### Features

- Initializes a square using a single size parameter.
- Validates size using the inherited integer_validator() method.
- Stores size as a private attribute.
- Calls the Rectangle constructor with equal width and height.
- Implements area() to calculate size multiplied by size.
- Inherits the string representation from Rectangle.

### Example

    s = Square(13)
    print(s)
    print(s.area())

Expected output:

    [Rectangle] 13/13
    169

### Concepts

- Multilevel inheritance
- Method overriding
- Polymorphism
- Encapsulation
- Code reuse through super()

## Task 5: Square #2

File: 2-square.py

This program extends the Square class by implementing
a custom string representation.

### Features

- Inherits from Rectangle.
- Validates size using integer_validator().
- Stores size as a private attribute.
- Initializes Rectangle with equal width and height.
- Implements area() to calculate the square's area.
- Overrides __str__() to display the square description.

### Example

    s = Square(13)
    print(s)
    print(s.area())

Expected output:

    [Square] 13/13
    169

### Concepts

- Inheritance
- Method overriding
- Polymorphism
- Encapsulation
- String representation using __str__()
