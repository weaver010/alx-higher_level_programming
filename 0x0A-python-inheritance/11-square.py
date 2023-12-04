#!/usr/bin/python3
"""Square class"""
Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """Square"""
    def __init__(self, size):
        """init square"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """return area"""
        return self.__size ** 2

    def __str__(self):
        """return string"""
        return "[Square] {}/{}".format(self.__size, self.__size)
