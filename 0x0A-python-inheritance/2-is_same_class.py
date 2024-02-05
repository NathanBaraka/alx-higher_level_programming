#!/usr/bin/python3
"""The definition of a class checking func """


def is_same_class(obj, a_class):
    """Verify whether an object precisely belongs to a specified class.

    Args:
    obj (any): The object to be examined.
    a_class (type): The class to compare with the type of obj.
    Returns:
    True if obj is strictly an instance of a_class; otherwise, False.
    """

    if type(obj) == a_class:
        return True
    return False
