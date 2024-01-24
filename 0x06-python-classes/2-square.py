#!/usr/bin/python3

"""Square class definition"""


class Square:
    """This is the square class"""

    def __init__(self, size):
        """New square initialization

        Args:
            size (int): New square size

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

