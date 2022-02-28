#!/usr/bin/python3
"""
Write a function that creates an Object
from a “JSON file”:
"""


def load_from_json_file(filename):
    """Reads a JSON file and creates a new object based on it"""
    import json
    with open(filename, mode='r') as file:
        return json.loads(file.read())
