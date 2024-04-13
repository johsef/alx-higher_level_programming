#!/usr/bin/python3
"""Definition of Student class"""


class Student:
    """Student class representation"""

    def __init__(self, first_name, last_name, age):
        """Public instance variables definition"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Returns attributes of class if found in attrs else
        print out all attribute of class Student"""
        if attrs is None:
            return(self.__dict__)
        else:
            dict_attrs = {}
            for attr in attrs:
                if hasattr(self, attr):
                    dict_attrs[attr] = getattr(self, attr)
            return (dict_attrs)

    def reload_from_json(self, json):
        """Replaces all attributes of the Student instance"""
        for key, value in json.items():
            setattr(self, key, value)
