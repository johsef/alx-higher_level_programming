#!/usr/bin/python3
"""Base class"""
import json
from os import path


class Base:
    """Base class definition"""

    __nb_objects = 0

    def __init__(self, id=None):
        """Base class Initializer"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
    
    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON string representation of list_dictionaries"""
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        else:
            return (json.dumps(list_dictionaries))

    @classmethod
    def save_to_file(cls, list_objs):
        """Method that writes the JSON representation of list_objs to a file"""
        file_name = cls.__name__ + ".json"
        new_list = []
        with open(file_name, 'w') as file:
            if list_objs is None:
                file.write("[]")
            for obj in list_objs:
                new_list.append(obj.to_dictionary())
            file.write(cls.to_json_string(new_list))

    @staticmethod
    def from_json_string(json_string):
        """Method that returns the list of the JSON string representation"""
        if json_string is None or json_string == "[]":
            return "[]"
        else:
            return(json.loads(json_string))

    @classmethod
    def create(cls, **dictionary):
        """Method that returns an instance with all attributes already set"""
        if cls.__name__ == 'Rectangle':
            new_class = cls(1, 1)
        else:
            new_class = cls(1)
        new_class.update(**dictionary)
        return new_class

    @classmethod
    def load_from_file(cls):
        """Method that returns a list of instances"""
        file_name = cls.__name__ + ".json"
        new_list = []
        return_list = []
        if path.isfile(file_name):
            with open(file_name, 'r') as file:
                new_list = cls.from_json_string(file.read())
            for value in new_list:
                return_list.append(cls.create(**value))
            return(return_list)
