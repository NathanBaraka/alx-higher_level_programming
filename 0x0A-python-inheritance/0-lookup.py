#!/usr/bin/python3
"""Definition of an obj attribute lookup func."""


def lookup(obj):
    """Return a list of of the obj attribute"""
    return (dir(obj))

