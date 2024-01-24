#!/usr/bin/python3

"""Module for the Square class"""

class Square:
    """Represents the square class."""

    def __init__(self, size=0):
        """
        Initializes a new Square instance.

        Args:
            size (int): The size of the square.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size should be int")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

