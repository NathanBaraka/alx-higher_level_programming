#!/usr/bin/python3
"""Defineation of a string-to-JSON func."""
import json


def to_json_string(my_obj):
    """Returns the JSON representation of a string object."""
    return json.dumps(my_obj)

