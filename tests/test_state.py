#!/usr/bin/python3
"""
test for state module
"""
from models.state import State
import unittest


class Test_State(unittest.TestCase):
    """
    test for the state class
    """
    def test_for_name(self):
        """ test the attr name length """
        self.assertTrue(hasattr(State, 'name'))
        self.assertIsInstance(State.name, str)
        self.assertEqual(0, len(State.name))
