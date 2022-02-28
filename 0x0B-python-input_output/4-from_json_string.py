#!/usr/bin/python3
"""
Write a function that returns the JSON
representation of an object (string)
"""


def from_json_string(my_str):
    """Append text to a file"""
    import json
    return json.loads(my_str)
