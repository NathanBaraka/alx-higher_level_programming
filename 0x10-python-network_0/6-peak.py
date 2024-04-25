#!/usr/bin/python3
""" This is an Algorithm for list of ints."""


def find_peak(list_of_integers):
    """Gets the peak in a list of unsorted integers."""
    if list_of_integers:
        list_of_integers.sort(reverse=True)
        return list_of_integers[0]
