#!/usr/bin/env python3
"""serializes instances to a JSON file and deserializes JSON file"""

import json
from os.path import exists
from datetime import datetime
from models.base_model import BaseModel
from models.user import User


class FileStorage:
    """serializes instances to a JSON file and deserializes JSON file"""
    __file_path = 'file.json'
    __objects = {}
    __cls_name = {"User": User, "BaseModel": BaseModel}

    def all(self):
        """ returns the dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """ sets in __objects the obj with key <obj class name>.id"""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file"""
        new_obj = {}
        for key, obj in FileStorage.__objects.items():
            new_obj[key] = obj.to_dict()
        with open(FileStorage.__file_path, 'w') as file:
            json.dump(new_obj, file)

    def reload(self):
        """deserializes the JSON file to"""
        try:
            with open(FileStorage.__file_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
            for key, value in data.items():
                cls_name = key.split(".")[0]
                if cls_name in FileStorage.__cls_name:
                    self.__objects[key] = self.__cls_name[cls_name](**value)
        except FileNotFoundError:
            pass
