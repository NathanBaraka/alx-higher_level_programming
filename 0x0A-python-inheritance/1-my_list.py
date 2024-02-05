#!/usr/bin/python3
"""Defines an inherited list class MyList."""

class MyList(list):
    """This does the implementation of the sorted prinitng for built in class."""

    def print_sorted(self):
        """List is printed in ascending order."""
        print(sorted(self))

