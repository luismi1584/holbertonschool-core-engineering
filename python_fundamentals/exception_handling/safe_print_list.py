#!/usr/bin/env python3
"""Safely print elements from a list."""


def safe_print_list(my_list=[], x=0):
    """Print up to x elements and return the number printed."""
    count = 0

    try:
        for i in range(x):
            print("{}".format(my_list[i]), end="")
            count += 1
    except IndexError:
        pass

    print()
    return count
