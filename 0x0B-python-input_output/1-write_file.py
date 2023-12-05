#!/usr/bin/python3
""" Write a file """


def write_file(filename="", text=""):
    """ Function that write a string to a text file 
        and return the umber of character written
    """
    with open(filename, 'w', encoding="utf-8") as f:
        f.write(text)
        return (len(text))
