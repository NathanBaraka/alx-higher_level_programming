#!/usr/bin/python3
def add_integer(a, b=98):
    """Add two integers.

    Args:
        a (int or float): The first integer or float.
        b (int or float, optional): The second integer or float (default is 98).

    Returns:
        int: The result of the addition.

    Raises:
        TypeError: If either a or b is a non-integer and non-float.
    """
    if ((not isinstance(a, int) and not isinstance(a, float))):
        raise TypeError("a must be an integer")
    if ((not isinstance(b, int) and not isinstance(b, float))):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))

