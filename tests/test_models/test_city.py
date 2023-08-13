#!/usr/bin/python3
"""
test for city module
"""
from models.city import City
import unittest


class Test_City(unittest.TestCase):
    """
    test for the city class
    """
    def test_for_doc(self):
        """
        tests if it has a documentation
        """
        self.assertIsNotNone(City.__doc__)

    def test_for_state_id(self):
        """
        tests for the input of state_id
        """
        self.assertTrue(hasattr(City, 'state_id'))
        self.assertIsInstance(City.state_id, str)
        self.assertEqual(0, len(City.state_id))

    def test_for_name(self):
        """ test the attr name length """
        self.assertTrue(hasattr(City, 'name'))
        self.assertIsInstance(City.name, str)
        self.assertEqual(0, len(City.name))
