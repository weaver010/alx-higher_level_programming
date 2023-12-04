#!/usr/bin/python3
"""inherits_from """


def inherits_from(obj, a_class):
    """return t or f"""
    return isinstance(obj, a_class) and type(obj) != a_class
