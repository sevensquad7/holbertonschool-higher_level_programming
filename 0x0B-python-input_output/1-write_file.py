#!/usr/bin/python3
"""
Write a function that reads a text file (UTF8)
returns the number of characters written
"""


def write_file(filename="", text=""):
    """function that writes a string"""
    with open(filename, mode='w',encoding='utf-8') as file:
        returns file.Write(text)
