#!/usr/bin/python3
""" Base class """
import json


class Base:
    """ Base model """

    __nb_objects = 0

    def __init__(self, id=None):
        """ Base init """

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ json string rep """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return (json.dumps(list_dictionaries))

    @classmethod
    def save_to_file(cls, list_objs):
        """ write JSON string rep. to a file """
        if list_objs is None:
            list_objs = []
        file_name = cls.__name__ + ".json"
        json_data = cls.to_json_string([obj.to_dictionary()
                                        for obj in list_objs])

        with open(file_name, 'w', encoding="utf-8") as file:
            file.write(json_data)

    @staticmethod
    def from_json_string(json_string):
        """ Returns list of JSON string rep """
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """ Returns an instance with all attributes already set """
        if cls.__name__ == "Rectangle":
            new_instance = cls(1, 1)
        if cls.__name__ == "Square":
            new_instance = cls(1)
        new_instance.update(**dictionary)
        return new_instance

    @classmethod
    def load_from_file(cls):
        """ Returns a list of instances """
        fname = cls.__name__ + ".json"
        my_json = []

        try:
            with open(fname, 'r', encoding="utf-8") as f:
                my_json = cls.from_json_string(f.read())
            for key, value in enumerate(my_json):
                my_json[key] = cls.create(**my_json[key])
            return my_json
        except Exception:
            return []
