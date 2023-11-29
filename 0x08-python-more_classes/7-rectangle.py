#!/usr/bin/python3

"""Rectangle Class.
"""


class Rectangle:
    """Defines  rectangle.
    """

    number_of_inst = 0
    print_window = "#"

    def __init__(self, width=0, height=0):
        """
        Args:
           width,height
        """
        Rectangle.number_of_inst += 1
        self.__width = width
        self.__height = height

    def __str__(self):
        """Return str"""
        if self.__height == 0 or self.__width == 0:
            return ""
        sstr = ""
        for i in range(self.__height):
            for j in range(self.__width):
                sstr += str(self.print_window)
            sstr += "\n"
        return sstr[:-1]

    def __repr__(self):
        """Return a string
        """
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """Print Bye ..."""
        Rectangle.n_of_inst -= 1
        print("Bye rectangle...")

    @property
    def width(self):
        """
        Returns:width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Arg:value
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        Return:height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Arg:value
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        Return:area
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        Return:perimeter
        """
        if self.width == 0 or self.height == 0:
            return 0
        else:
            return 2 * (self.__width + self.__height)
