#!/usr/bin/python3
"""square class."""
from models.rectangle import Rectangle


class Square(Rectangle):
    """square."""

    def __init__(self, size, x=0, y=0, id=None):
        """
        Args:
            size,x,y,id
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Get the size"""
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Update the Square.

        Args:
            *args,**kwargs
        """
        if args and len(args) != 0:
            e = 0
            for t in args:
                if e == 0:
                    if t is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = t
                elif e == 1:
                    self.size = t
                elif e == 2:
                    self.x = t
                elif e == 3:
                    self.y = t
                e += 1

        elif kwargs and len(kwargs) != 0:
            for i, u in kwargs.items():
                if i == "id":
                    if u is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = u
                elif i == "size":
                    self.size = u
                elif i == "x":
                    self.x = u
                elif i == "y":
                    self.y = u

    def to_dictionary(self):
        """Return the dictionary"""
        return {
            "id": self.id,
            "size": self.width,
            "x": self.x,
            "y": self.y
        }

    def __str__(self):
        """Return the print() and str()"""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y,
                                                 self.width)
