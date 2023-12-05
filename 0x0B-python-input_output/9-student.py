#!/usr/bin/python3
"""class Student"""


class Student:
    """
    Class Studentt.
    """
    def __init__(self, first_name, last_name, age):
        """Args:
            first_name : first name
            last_name : last name
            age : age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        Return: dict
        """
        return self.__dict__
