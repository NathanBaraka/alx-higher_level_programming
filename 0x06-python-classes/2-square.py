#!/usr/bin/python3

"""Class defination"""


class Square:
    """Represents the square class"""

    def __init__(self, size=0):
        """Initialization of a new Square.

        Args:
            size (int): New square size.
        """
        if not isinstance(size, int):
            raise TypeError("size should be int")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

