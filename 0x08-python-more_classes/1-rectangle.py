#!/usr/bin/python3
"""class Rectangle"""


class Rectangle:
    """
    rectangle
    """
    def __init__(self, width=0, height=0):
        """
        Args:width, height
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        Return: width
        """
        return self.__width

    @property
    def height(self):
        """
        Return:height
        """
        return self.__height

    @width.setter
    def width(self, value):
        """
        Args:value
        Raises:TypeError,ValueError
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @height.setter
    def height(self, value):
        """
        Args:value

        Raises:TypeError,ValueError
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value
