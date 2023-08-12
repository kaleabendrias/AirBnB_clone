#!/usr/bin/python3

"""
this module is used and serializing and deserializing
json files
"""
import json


class FileStorage:
    """
    a filestorage class that helps
    in serializing and deserializing json files
    and also saving the data in them
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        returns the dictionary __objects
        """
        return (FileStorage.__objects)

    def new(self, obj):
        """
        adds the obj in the __object dict
        """
        key = f"{obj.__class__.__name__}.{obj.id}"
        if key not in FileStorage.__objects.keys():
            FileStorage.__objects[key] = obj.to_dict()

    def save(self):
        """
        it is used to serialize objects
        the json __file_path
        """
        with open(FileStorage.__file_path, "w") as file:
            json.dump(FileStorage.__objects, file)

    def reload(self):
        """
        it is used to load json data
        from json files
        """
        try:
            with open(FileStorage.__file_path, "r") as file:
                jsonData = json.load(file)
                FileStorage.__objects.update(jsonData)
        except FileNotFoundError:
            pass
