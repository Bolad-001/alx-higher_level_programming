#!/usr/bin/python3
""" Sorted Function"""


class MyList(list):
    """ Class to inherit """

    def print_sorted(self):
        """ print list """
        print(sorted(self))
