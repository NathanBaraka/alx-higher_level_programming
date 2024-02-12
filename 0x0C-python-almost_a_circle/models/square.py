#!/usr/bin/python3
"""
Defination of a square class.
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Representation of a square.
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        Initialization of a new Square.
        """
        super().__init__(size, size, x, y, id)
