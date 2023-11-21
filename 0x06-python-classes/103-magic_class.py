#!/usr/bin/python3
"""class MagicClass"""
import math


class MagicClass:
    """circle"""
    def __init__(self, radius=0):
        """
        Arg:
            radius : radius
        """
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')
        self.__radius = radius

    def area(self):
        """
        Return :the area
         """
        return (self.__radius ** 2) * math.pi

    def circumference(self):
        """
        Return:The circumference
        """
        return (2 * math.pi * self.__radius) 
