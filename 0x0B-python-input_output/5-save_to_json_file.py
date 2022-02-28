#!/usr/bin/python3
"""
Write a function that writes an Object to a text file
using a JSON representation
"""


def save_to_json_file(my_obj, filename):
    """Writes an Object to a text file"""
    import json
    with open(filename, mode='w') as file:
        json.dump(my_obj, file)
