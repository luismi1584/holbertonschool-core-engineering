# Python - Exception Handling

This module covers Python exception handling and writing
defensive, predictable programs.

## Learning Objectives

- Identify common runtime exceptions.
- Use try and except blocks.
- Catch specific exception types.
- Use else and finally blocks.
- Raise exceptions explicitly.
- Handle errors safely.

## Tasks

### 0. Safe List Printing
- File: safe_print_list.py
- Prints up to x elements of a list.
- Handles IndexError using try and except.
- Returns the actual number of elements printed.

### 1. Safe Integer Printing
- File: safe_print_integer.py
- Prints integers using "{:d}".format().
- Returns True when printing succeeds.
- Returns False when formatting raises an exception.
- Uses try and except without importing modules or using type().

### 2. Safe List Printing with Type Handling
- File: safe_print_list_integers.py
- Prints only integers among the first x elements of a list.
- Skips non-integer elements using try and except.
- Returns the number of integers successfully printed.
- Allows IndexError to propagate when x exceeds the list length.
