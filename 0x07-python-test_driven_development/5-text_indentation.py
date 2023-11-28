#!/usr/bin/python3

def text_indentation(text):
    """
    Print text
    args:text
    Raises:TypeError
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    u = text[:]
    for delm in ".?:":
        o = u.split(delm)
        u = ""
        for i in o:
            i = i.strip(" ")
            if u is "":
                u = i + delm
            else:
                u = u + "\n\n" + i + delm
    print(u[:-3], end="")
