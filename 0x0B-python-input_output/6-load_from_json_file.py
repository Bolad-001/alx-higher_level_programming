#!/usr/bin/python3
""" Object from Json """
import json


def load_from_json_file(filename):
    """ Function that create an
        object from JSON file
    """
    with open(filename, 'r') as f:
        obj = json.load(f)
        return (obj)
