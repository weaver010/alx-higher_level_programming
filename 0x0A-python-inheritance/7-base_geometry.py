#!/usr/bin/python3
"""BaseGeometry class"""


class BaseGeometry():
    """BaseGeometry """
    def area(self):
        """Raises an Exception message"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ int valid"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
