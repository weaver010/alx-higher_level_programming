#!/usr/bin/python3
""" class Square"""


class Square:
    """
    Attributes:
        __size : size
    """
    def __init__(self, size=0):
        """
        Args:
            size : size

        Returns:
            None
        """
        self.size = size

    def area(self):
        """
        Returns: area
        """
        return (self.__size) * (self.__size)

    @property
    def size(self):
        """
        Returns: size
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Args:
            value : size

        Returns: None
        """
        if type(value) != int:
            raise TypeError("size must be an integer")
        else:
            if value < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = value
