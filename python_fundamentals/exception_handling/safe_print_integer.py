#!/usr/bin/env python3
"""Safely print an integer."""


def safe_print_integer(value):
    """Print an integer and return True, or False if invalid."""
    try:
        print("{:d}".format(value))
        return True
    except (ValueError, TypeError):
        return False
