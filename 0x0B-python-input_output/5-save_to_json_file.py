#!/usr/bin/python3
""" Object to text """
import json


def save_to_json_file(my_obj, filename):
    """ fucntion that writes an object to a
        text file
    """
    with open(filename, 'w', encoding='utf-8') as f:
        return (json.dump(my_obj, f))
