#!/usr/bin/python3
"""Defines an inherited class-checking func."""


def inherits_from(obj, a_class):
    """Determine whether an object is an inherited instance of a specified class.

    Args:
    obj (any): The object to be examined.
    a_class (type): The class to compare with the type of obj.
    Returns:
    True if obj is an inherited instance of a_class; otherwise, False.
    """

    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False

