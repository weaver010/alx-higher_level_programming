#!/usr/bin/python3
"""class Square"""


class Square:
    """
    Attributes:
        __size : size
        __position ): position
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Args:
            size : size
            position : positoin

        Returns: None
        """
        self.size = size
        self.position = position

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
        if type(value) is not int:
            raise TypeError("size must be an integer")
        else:
            if value < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = value

    @property
    def position(self):
        """
        Returns : position
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Args:
            value : position

        Return:
            None
        """
        if type(value) != tuple or len(value) != 2 or \
                type(value[0]) != int or value[0] < 0 or \
                type(value[1]) != int or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def my_print(self):
        """print square
        """

        if self.__size == 0:
            print()
        else:
            for i in range(self.__position[1]):
                print()
            for j in range(self.__size):
                for o in range(self.__position[0]):
                    print(" ", end="")
                print("#" * (self.__size))
