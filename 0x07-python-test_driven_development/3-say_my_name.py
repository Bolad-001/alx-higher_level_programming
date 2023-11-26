#!/usr/bin/python3

"""Function that prints name"""


def say_my_name(first_name, last_name=""):
    """ print first and last name

    Args:
        first_name: first name to print
        last_name: last name to print

    """
    if type(first_name) != str:
        raise TypeError("first_name must be a string")
    if type(last_name) != str:
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))
