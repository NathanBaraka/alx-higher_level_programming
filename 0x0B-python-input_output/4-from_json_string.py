#!/usr/bin/python3
# 6-from_json_string.py
"""Defination of a JSON-to-object func."""
import json


def from_json_string(my_str):
    """Returns the Python object representation of a JSON string."""
    return json.loads(my_str)
