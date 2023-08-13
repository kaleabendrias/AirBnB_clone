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
