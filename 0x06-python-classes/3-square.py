#!/usr/bin/python3

"""Define a class Square."""

class Square:
    """Represents a square.

    Attributes:
        __size (int): The size of the square.

    Methods:
        __init__(self, size=0): Initializes a new square.
        area(self): Returns the current area of the square.
    """

    def __init__(self, size=0):
        """Initializes a new square.

        Args:
            size (int): The size of the new square.
        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Returns the current area of the square."""
        return self.__size * self.__size

