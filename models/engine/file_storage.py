#!/usr/bin/env python3
"""serializes instances to a JSON file and deserializes JSON file"""

import json
from os.path import exists
from datetime import datetime


class FileStorage:
    """serializes instances to a JSON file and deserializes JSON file"""
    __file_path = 'file.json'
    __objects = {}

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
        """deserializes the JSON file to __objects:"""
        if exists(FileStorage.__file_path):
            with open(FileStorage.__file_path, 'r') as file:
                obj_dict = json.load(file)
                from models.base_model import BaseModel

                for key, value in obj_dict.items():
                    cls_name, obj_id = key.split('.')
                    cls = BaseModel if cls_name == 'BaseModel' else None
                    if cls:
                        value['created_at'] = datetime.fromisoformat(value['created_at'])
                        value['updated_at'] = datetime.fromisoformat(value['updated_at'])
                        obj = cls(*value)
                        self.new(obj)
