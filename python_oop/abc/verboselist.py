#!/usr/bin/env python3
"""Extend Python's built-in list with modification notifications."""


class VerboseList(list):
    """A list that prints messages when items are added or removed."""

    def append(self, item):
        """Append an item and print a notification."""
        super().append(item)
        print("Added [{}] to the list.".format(item))

    def extend(self, iterable):
        """Extend the list and print the number of items added."""
        items = list(iterable)
        super().extend(items)
        print("Extended the list with [{}] items.".format(len(items)))

    def remove(self, item):
        """Print a notification before removing an item."""
        if item not in self:
            raise ValueError("list.remove(x): x not in list")
        print("Removed [{}] from the list.".format(item))
        super().remove(item)

    def pop(self, index=-1):
        """Print a notification before popping an item."""
        item = self[index]
        print("Popped [{}] from the list.".format(item))
        return super().pop(index)
