#!/usr/bin/python3
"""base geo"""


class BaseGeometry:
    """Base geo"""
    def area(self):
        """area"""
        raise Exception("area() is not implemented")
    def integer_validator(self, name, value):
        """check value"""
        if type(value) is not int:
            raise TypeError("age must be an integer")
        if value <= 0:
            raise ValueError("age must be greater than 0")
