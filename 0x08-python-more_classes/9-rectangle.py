#!/usr/bin/python3
"""Rectangle Class.
"""


class Rectangle:
    """Defines  rectangle.
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """
        Args:
           width,height
        """
        type(self).number_of_instances += 1
        self.width = width
        self.height = height

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
        return (self.__width * self.__height)

    def perimeter(self):
        """
        Return:perimeter
        """
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__width * 2) + (self.__height * 2))

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        Arg:
            rect_1,rect_2
        Raise:
            TypeError
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return (rect_1)
        return (rect_2)

    @classmethod
    def square(cls, size=0):
        """
        Arg:size
        """
        return (cls(size, size))

    def __str__(self):
        """Return str"""
        if self.__width == 0 or self.__height == 0:
            return ("")

        sstr = []
        for i in range(self.__height):
            [sstr.append(str(self.print_symbol)) for j in range(self.__width)]
            if i != self.__height - 1:
                sstr.append("\n")
        return ("".join(sstr))

    def __repr__(self):
        """Return a string
        """
        sstr = "Rectangle(" + str(self.__width)
        sstr += ", " + str(self.__height) + ")"
        return (sstr)

    def __del__(self):
        """Print Bye ..."""
        type(self).number_of_instances -= 1
        print("Bye rectangle...")