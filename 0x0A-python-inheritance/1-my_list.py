#!/usr/bin/python3
"""MyList"""


class MyList(list):
    """
	Inherits list
    """
    def print_sorted(self):
        """Prints list"""
        print(sorted(self))
