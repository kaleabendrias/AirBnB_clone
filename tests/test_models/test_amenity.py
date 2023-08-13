#!/usr/bin/python3
"""
test for amenity module
"""
from models.amenity import Amenity
import unittest


class Test_Amenity(unittest.TestCase):
    """
    test for the amenity class
    """
    def test_for_name(self):
        """ test the attr name length """
        self.assertTrue(hasattr(Amenity, 'name'))
        self.assertIsInstance(Amenity.name, str)
        self.assertEqual(0, len(Amenity.name))
