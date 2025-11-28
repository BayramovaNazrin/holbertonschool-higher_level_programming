#!/usr/bin/python3
"""base geo"""


class BaseGeometry:
    """Base geo"""
    def area(self):
        """area"""
        raise Exception("area() is not implemented")
    def integer_validator(self, name, value):
        """check value"""
        if value is not int:
            raise TypeError("<name> must be an integer")
        if value is <= 0:
            raise ValueError("<name> must be greater than 0")
