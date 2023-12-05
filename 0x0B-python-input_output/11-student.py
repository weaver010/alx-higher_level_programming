#!/usr/bin/python3
"""class Student"""


class Student:
    """
    class students
    """
    def __init__(self, first_name, last_name, age):
        """
	Args:
            first_name : first name
            last_name : last name
            age : age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Returns:dict
        """
        if attrs is None:
            return self.__dict__

        d = {}
        for i in attrs:
            try:
                d[i] = self.__dict__[i]
            except Exception:
                pass
        return d
    def reload_from_json(self, json):
        """
        Args:
            json : json
        """
        self.__dict__.update(json)
