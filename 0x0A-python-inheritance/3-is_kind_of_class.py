#!/usr/bin/python3
"""Defines a class and inherited class-checking func """


def is_kind_of_class(obj, a_class):
    """Determine whether an object is an instance or inherits from a specified class.

    Args:
    obj (any): The object to be examined.
    a_class (type): The class to compare with the type of obj.
    Returns:
    True if obj is an instance or an inherited instance of a_class; else, False.
    """

    if isinstance(obj, a_class):
        return True
    return False

