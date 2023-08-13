#!/usr/bin/usr/python3

"""
this is a test file
for the module base_model.py
base of all other classes
"""

import datetime
from models.base_model import BaseModel
from models import storage
import unittest
import uuid


class Test_BaseModel(unittest.TestCase):
    """
    this is the class used in testing the basemodel
    """
    def setUp(self):
        """
        it is initialised each and everytime a
        test method runs
        """
        self.model1 = BaseModel()

    def tearDown(self):
        """
        it cleans up after the setUp funtion
        """
        pass

    def test_for_attributes_(self):
        """
        this test method is used to test the attr of the  base model
        """
        self.assertTrue(uuid.UUID(self.model1.id, version=4))
        self.assertIsInstance(self.model1.created_at, datetime.datetime)
        self.assertIsInstance(self.model1.updated_at, datetime.datetime)
        # for typed input
        model2 = BaseModel(created_at="2023-08-07T21:50:34.333")
        self.assertIsInstance(self.model1.created_at, datetime.datetime)

    def test_for__str__(self):
        """
        this is a test for the function
        __str__
        """
        expectedStr = f"[BaseModel] ({self.model1.id}) {self.model1.__dict__}"
        self.assertEqual(str(self.model1), expectedStr)

    def test_for_save(self):
        """
        test for the method save
        """
        initial = self.model1.updated_at
        self.model1.save()
        self.assertNotEqual(self.model1.updated_at, initial)
        dictOfObj = storage.all()
        obj = self.model1
        key = f"{obj.__class__.__name__}.{obj.id}"
        del dictOfObj[key]
        storage.save()

    def test_for_to_dict(self):
        """
        tests for to_dict method
        it checks if:
        1. type dict is returned
        2. if it contains the key__class__ and correct value
        3. make sure no other items apart from the attr are there
        """
        model1Dict = self.model1.to_dict()
        self.assertIsInstance(model1Dict, dict)
        self.assertEqual(model1Dict["__class__"], "BaseModel")
        for item in model1Dict.keys():
            if item not in (self.model1.__dict__.keys()):
                if item == "__class__":
                    continue
                self.fail(f"key {item} not an attr")
