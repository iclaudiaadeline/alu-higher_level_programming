#!/usr/bin/python3
"""
This module contains a function that reads a text file and prints it .
"""

def read_file(filename=""):
    """Reads a text file.
    args:
         filename: name of the file
    """


    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
