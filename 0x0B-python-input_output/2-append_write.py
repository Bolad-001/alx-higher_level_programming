#!/usr/bin/python3
""" Append a string """


def append_write(filename="", text=""):
    """ Function that append a string at the end of a text
        file and return the number of characters added
    """
    with open(filename, 'a', encoding="utf-8") as f:
        f.write(text)
        return (len(text))
