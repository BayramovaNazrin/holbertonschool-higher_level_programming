#!/usr/bin/python3
"""check if object is sub-class, not the class itself!"""


def inherits_from(obj, a_class):
    """chech inherits"""
    return issubclass(obj, a_class)
