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

## Task 1: Shapes, Interfaces, and Duck Typing

File: `shapes.py`

### Description

Demonstrates abstract base classes, geometric calculations,
inheritance, polymorphism, and duck typing.

### Classes

- Shape: Abstract base class defining area() and perimeter().
- Circle: Implements area() and perimeter() using its radius.
- Rectangle: Implements area() and perimeter() using its
  width and height.

### Function

- shape_info(shape): Prints the area and perimeter of an
  object using its methods without checking its type.

### Example

    from shapes import Circle, Rectangle, shape_info

    circle = Circle(radius=5)
    rectangle = Rectangle(width=4, height=7)

    shape_info(circle)
    shape_info(rectangle)

Expected output:

    Area: 78.53981633974483
    Perimeter: 31.41592653589793
    Area: 28
    Perimeter: 22

### Concepts

- Abstract Base Classes (ABC)
- Abstract methods
- Inheritance and polymorphism
- Duck typing
- Geometric calculations

## Task 2: The Enigmatic FlyingFish - Exploring Multiple Inheritance

File: `flyingfish.py`

### Description

Demonstrates multiple inheritance and Python's Method Resolution
Order (MRO) using Fish, Bird, and FlyingFish classes.

### Classes

- Fish: Defines swim() and habitat() methods.
- Bird: Defines fly() and habitat() methods.
- FlyingFish: Inherits from Fish and Bird and overrides
  swim(), fly(), and habitat().

### Example

    from flyingfish import Fish, Bird, FlyingFish

    flying_fish = FlyingFish()

    flying_fish.swim()
    flying_fish.fly()
    flying_fish.habitat()

Expected output:

    The flying fish is swimming!
    The flying fish is soaring!
    The flying fish lives both in water and the sky!

### Method Resolution Order

The MRO of FlyingFish is:

    FlyingFish
    Fish
    Bird
    object

Python searches classes in this order when resolving inherited
methods and attributes.

### Concepts

- Multiple inheritance
- Method overriding
- Method Resolution Order (MRO)
- Polymorphism
- Parent and child classes

## Task 3: The Mystical Dragon - Mastering Mixins

File: `dragon.py`

### Description

Demonstrates how mixins provide reusable behaviors through
multiple inheritance.

The Dragon class inherits swimming and flying capabilities
from two separate mixins.

### Classes

- SwimMixin: Provides the swim() method.
- FlyMixin: Provides the fly() method.
- Dragon: Inherits from SwimMixin and FlyMixin and defines
  its own roar() method.

### Example

    from dragon import Dragon

    dragon = Dragon()

    dragon.swim()
    dragon.fly()
    dragon.roar()

Expected output:

    The creature swims!
    The creature flies!
    The dragon roars!

### Method Resolution Order

The MRO of Dragon is:

    Dragon
    SwimMixin
    FlyMixin
    object

### Concepts

- Mixins
- Multiple inheritance
- Reusable behaviors
- Method Resolution Order (MRO)
- Code composition
