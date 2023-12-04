#!/usr/bin/python3
"""Rectangle class"""
BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle"""
    def __init__(self, width, height):
        """init rectangle"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """returns area"""
        area = self.__width * self.__height
        return area

    def __str__(self):
        """Returns string"""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
