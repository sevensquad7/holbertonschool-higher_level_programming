#!/usr/bin/python3
"""
Write a function that reads a text file (UTF8)
returns the number of characters added
"""


def append_write(filename="", text=""):
    """function that appends a string"""
    with open(filename, mode='a', encoding='utf-8') as file:
        return file.write(text)
