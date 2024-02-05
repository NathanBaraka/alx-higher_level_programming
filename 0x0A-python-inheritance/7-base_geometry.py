#!/usr/bin/python3
"""Defines a base geometry class BaseGeometry."""


class BaseGeometry:
    """Reprsent base geometry."""

    def area(self):
        """Not yet implemented."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
       """Verify a parameter to ensure it is an integer.

    Args:
    name (str): The name of the parameter.
    value (int): The parameter to be validated.
    Raises:
    TypeError: If the value is not an integer.
    ValueError: If the value is less than or equal to zero.
    """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
