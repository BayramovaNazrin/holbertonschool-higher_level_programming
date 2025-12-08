#!/usr/bin/python3
"""Module for append_write function"""


def append_write(filename="", text=""):
    """Append a string to the end of a UTF-8 file and return number of characters added."""
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
