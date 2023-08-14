#!/usr/bin/python3

"""
this module tests for methods and attr
in FileStorage class
"""

from models.engine.file_storage import FileStorage
from models import storage
from models.base_model import BaseModel
import json
import os
import unittest


class Test_for_FileStorage(unittest.TestCase):
    """
    this is a class that deals with in
    testing the methods and attr of FileStorage
    """
    storage = storage

    def setUp(self):
        """
        setUp method;
        opens file and manipulates each as per test
        """
        self.model1 = BaseModel()
        storage.new(self.model1)
        storage.save()

    def tearDown(self):
        """
        cleans up created file by setUp
        """
        dictOfObj = storage.all()
        obj = self.model1
        key = f"{obj.__class__.__name__}.{obj.id}"
        del dictOfObj[key]
        storage.save()

    def test__objects(self):
        """
        tests the existence of the attr __objects
        """
        self.assertIsInstance(self.storage._FileStorage__objects, dict)

    def test__file_path(self):
        """
        tests the existence of the attr __file_path
        """
        self.assertEqual(self.storage._FileStorage__file_path, "file.json")

    def test_for_all(self):
        """
        tests the returned dictionary __objects
        """
        self.assertTrue(len(storage.all()))

    def test_for_new(self):
        """
        checks if a new object has been added in the dict
        """
        obj = self.model1
        storage.new(obj)
        key = f"{obj.__class__.__name__}.{obj.id}"
        if key not in storage.all().keys():
            self.fail("object not inserted")

    def test_for_save(self):
        """
        tests for file existence
        """
        if os.path.exists("file.json"):
            pass
        else:
            self.fail("file does not exist")

    def test_reload(self):
        """Test the reload method"""
        base_model = BaseModel()
        self.storage.new(base_model)
        self.storage.save()
        with open("file.json", "r") as file:
            text = file.read()
            self.assertIn("BaseModel." + base_model.id, text)

        base_model.name = "Updated name"
        base_model.save()

        new_storage = FileStorage()
        new_storage.reload()
        key = "{}.{}".format(base_model.__class__.__name__, base_model.id)
        self.assertIn(key, self.storage._FileStorage__objects)
        reloaded_ins = new_storage.all()[key]
