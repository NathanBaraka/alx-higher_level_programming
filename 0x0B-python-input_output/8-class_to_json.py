#!/usr/bin/python3
"""Defination of a Python class-to-JSON func."""


def class_to_json(obj):
    """Returns the dictionary represntation of a simple data structure."""
    return obj.__dict__
