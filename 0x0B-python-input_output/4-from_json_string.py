#!/usr/bin/python3
""" JSON representation
"""
import json


def from_json_string(my_str):
    """ Function that returns an object by a JSON representation """
    return json.loads(my_str)
