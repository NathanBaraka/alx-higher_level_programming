#!/usr/bin/python3
"""
Defination of a base model class.
"""
import json
import csv
import turtle

class Base:
    """
    Representation of the base model
    """
    __nb_objects = 0
    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON string representation of list_dictionaries.
        Args:
            list_dictionaries (list): A list of dictionaries.
        """
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        to_json = json.dumps(list_dictionaries)

        return to_json
    @classmethod
    def save_to_file(cls, list_objs):
        """Writes the JSON string representation of list_objs to a file.
        Args:
            list_objs (list): List of instances who inherits of Base
        """
        file_name = "{}.json".format(cls.__name__)

        with open(file_name, "w") as jsonfile:
            if list_objs is None:
                jsonfile.write("[]")
            else:
                list_dict = []
                for obj in list_objs:
                    list_dict.append(obj.to_dictionary())
                jsonfile.write(Base.to_json_string(list_dict))

    def from_json_string(json_string):
    """
    Deserialize a JSON-formatted string and return the corresponding Python object.

    Parameters:
    - json_string (str): A JSON-formatted string to be deserialized.

    Returns:
    - obj: The Python object resulting from deserialization.

    If the input `json_string` is None or an empty list representation ("[]"), an empty list is returned.

    """
    if json_string is None or json_string == "[]":
        return []
    return json.loads(json_string)

   
