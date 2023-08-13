#!/usr/bin/python3

"""
this is unittest for console.py
"""

from console import HBNBCommand
from models import storage
# ast: changes a str to literal datatype "[1, 2, 3]" -> [1, 2, 3]
import ast
import json
from io import StringIO
import unittest
from unittest.mock import patch


class Test_Console(unittest.TestCase):
    """
    tests console class to check if the required output
    is actually what is the output
    """
    def get_obj_of_a_class(cls, dictOfAllObjects, specifiedClass):
         """ gets all objects for a specific class """
         objectsDictionary = {}
         for key in dictOfAllObjects.keys():
             if dictOfAllObjects[key]["__class__"] == specifiedClass:
                 objectsDictionary[key] = dictOfAllObjects[key]
         return (objectsDictionary)

    def stdout_tester(self, cmd, expected):
        """
        so this function takes all arguments passed into it and 
        checks it  with the expected input
        """

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("User.all()")
            parsed_list = ast.literal_eval(f.getvalue())
            self.assertEqual(len(parsed_list), len(expected))

    def test_for_all_format1(self):
        """
        checks if all command gives all input with and without adding BaseModel
        """
        with open("file.json", "r+") as f:
            expected = json.load(f)
        self.stdout_tester("all", expected)
