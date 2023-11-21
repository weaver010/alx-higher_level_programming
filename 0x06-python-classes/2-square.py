#!/usr/bin/python3
"""class Square"""


class Square:
    """
    Attributes:
        __size : size

    """
    def __init__(self, size=0):
        """
        Args:
            size: size

        Returns: None
        """
        if type(size) != int:
            raise TypeError("size must be an integer")
        else:
            if size < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = size
