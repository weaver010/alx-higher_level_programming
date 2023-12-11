#!/usr/bin/python3
"""rectangle class."""
from models.base import Base


class Rectangle(Base):
    """rectangle"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Args:
            width,height,x,y,id
        Raise:
            TypeError,ValueError,TypeError,ValueError
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """Set the width"""
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Set the height """
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Set the x coordinate """
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Set the y coordinate"""
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Return the area"""
        return self.width * self.height

    def display(self):
        """Print the #"""
        if self.width == 0 or self.height == 0:
            print("")
            return

        [print("") for k in range(self.y)]
        for i in range(self.height):
            [print(" ", end="") for b in range(self.x)]
            [print("#", end="") for z in range(self.width)]
            print("")

    def update(self, *args, **kwargs):
        """
        Arg:
            *args
            **kwargs
        """
        if args and len(args) != 0:
            t = 0
            for p in args:
                if t == 0:
                    if p is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = p
                elif t == 1:
                    self.width = p
                elif t == 2:
                    self.height = p
                elif t == 3:
                    self.x = p
                elif t == 4:
                    self.y = p
                t += 1

        elif kwargs and len(kwargs) != 0:
            for i, u in kwargs.items():
                if i == "id":
                    if u is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = u
                elif i == "width":
                    self.width = u
                elif i == "height":
                    self.height = u
                elif i == "x":
                    self.x = u
                elif i == "y":
                    self.y = u

    def to_dictionary(self):
        """Return the dictionary"""
        return {
            "id": self.id,
            "width": self.width,
            "height": self.height,
            "x": self.x,
            "y": self.y
        }

    def __str__(self):
        """Return the print() and str()."""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id,
                                                       self.x, self.y,
                                                       self.width, self.height)
