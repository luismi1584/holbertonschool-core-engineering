#!/usr/bin/env python3
"""Print integers safely from a list."""


def safe_print_list_integers(my_list=[], x=0):
    """Print integers among the first x elements of a list."""
    count = 0

    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
            count += 1
        except (TypeError, ValueError):
            pass

    print()
    return count
