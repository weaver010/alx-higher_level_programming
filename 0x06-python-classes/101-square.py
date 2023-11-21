#!/usr/bin/python3

"""class Square."""


class Square:
    """square"""

    def __init__(self, size=0, position=(0, 0)):
        """
        Args:
            size : size
            position: The position
        """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """
        Returns: position
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Args:
            value : position

        Returns: None
        """
        if type(value) is not tuple or len(value) != 2 or \
                type(value[0]) is not int or value[0] < 0 or \
                type(value[1]) is not int or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """
        Return : area
        """
        return (self.__size) * (self.__size)

    def my_print(self):
        """Print the square."""
        if self.__size == 0:
            print("")
            return

        else:
            for i in range(self.__position[1]):
                print()
            for j in range(self.__size):
                for o in range(self.__position[0]):
                    print(" ", end="")
                print("#" * (self.__size))

    def __str__(self):
        """Square."""
        if self.__size == 0:
            return ""
        s = "\n" * self.position[1]
        p = (" " * self.position[0] + "#" * self.size + "\n") * self.size
        a = s + p
        return a[:-1]
