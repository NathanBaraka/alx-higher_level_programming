#!/usr/bin/python3
"""Defination of a JSON file-writing func."""
import json


def save_to_json_file(my_obj, filename):
    """Writes an object to a text file using JSON representation."""
    with open(filename, "w") as f:
        json.dump(my_obj, f)

