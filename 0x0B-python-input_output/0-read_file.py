#!/usr/bin/python3
"""Defination of  a txt file-reading func."""


def read_file(filename=""):
    """Prints the contents of a UTF8 text file to stdout."""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")

