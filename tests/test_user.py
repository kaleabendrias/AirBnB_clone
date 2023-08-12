#!/usr/bin/python3
"""
test for user module
"""
from models.user import User
import unittest


class Test_User(unittest.TestCase):
    """
    test for the user class
    """
    def test_for_email(self):
        """ test the attr email """
        self.assertTrue(hasattr(User, 'email'))
        self.assertIsInstance(User.email, str)
        self.assertEqual(0, len(User.email))

    def test_for_password(self):
        """ test the attr password """
        self.assertTrue(hasattr(User, 'password'))
        self.assertIsInstance(User.password, str)
        self.assertEqual(0, len(User.password))

    def test_for_first_name(self):
        """ test the attr first name  """
        self.assertTrue(hasattr(User, 'first_name'))
        self.assertIsInstance(User.first_name, str)
        self.assertEqual(0, len(User.first_name))

    def test_for_name(self):
        """ test the attr last name """
        self.assertTrue(hasattr(User, 'last_name'))
        self.assertIsInstance(User.last_name, str)
        self.assertEqual(0, len(User.last_name))
