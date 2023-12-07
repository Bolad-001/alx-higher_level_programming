#!/usr/bin/python3
""" class_to_json """


def class_to_json(obj):
    """Creates a dict description of obj
    """
    return obj.__dict__
