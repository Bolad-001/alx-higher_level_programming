#!/usr/bin/python3
""" Read file """


def read_file(filename=""):
    """ Function that read a file and print it to stdout """

    with open(filename, encoding='utf-8') as f:
        for line in f:
            print(line, end='')
