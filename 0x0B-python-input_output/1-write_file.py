#!/usr/bin/python3
"""Defination of a file-writing func."""


def write_file(filename="", text=""):
    """Write a string to a UTF8 text file.

    Args:
        filename (str): File name to be written.
        text (str): Text to write.
    Returns:
        The number of characters written.
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)

