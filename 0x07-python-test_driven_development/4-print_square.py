#!/usr/bin/python3

"""
    Function that print square
"""


def print_square(size):
    """
        print square with char "#"

    Args:
        size: size of square
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if isinstance(size, float):
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        print("#" * size)
