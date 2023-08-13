#!/usr/bin/python3

"""
this is a module used to test the console
"""

import unittest
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand


class TestConsole(unittest.TestCase):
    """
    Test suite for the HBNBCommand class in the console module.
    """

    def setUp(self):
        """
        Set up the test environment by creating an instance of HBNBCommand.
        """
        self.console = HBNBCommand()

    def test_create(self):
        """
        Test the 'create' command of the console.
        Checks if the command creates an instance and prints its ID.
        """
        with patch('sys.stdout', new=StringIO) as mock_stdout:
            self.console.onecmd("create BaseModel")
            output = mock_stdout.getvalue().strip()
            self.assertTrue(len(output) > 0)

    def test_show(self):
        """
        Test the 'show' command of the console.
        Checks if the command prints the correct
        message when instance ID is missing.
        """
        with patch('sys.stdout', new=StringIO) as mock_stdout:
            self.console.onecmd("show BaseModel")
            output = mock_stdout.getvalue().strip()
            self.assertEqual(output, "** instance id missing **")

    def test_destroy(self):
        """
        Test the 'destroy' command of the console.
        Checks if the command prints the correct
        message when instance ID is missing.
        """
        with patch('sys.stdout', new=StringIO) as mock_stdout:
            self.console.onecmd("destroy BaseModel")
            output = mock_stdout.getvalue().strip()
            self.assertEqual(output, "** instance id missing **")

    def test_all(self):
        """
        Test the 'all' command of the console.
        Checks if the command prints a list of all instances.
        """
        with patch('sys.stdout', new=StringIO) as mock_stdout:
            self.console.onecmd("all")
            output = mock_stdout.getvalue().strip()
            self.assertTrue(len(output) > 0)

    def test_update(self):
        """
        Test the 'update' command of the console.
        Checks if the command prints the correct
        message when instance ID is missing.
        """
        with patch('sys.stdout', new=StringIO) as mock_stdout:
            self.console.onecmd("update BaseModel")
            output = mock_stdout.getvalue().strip()
            self.assertEqual(output, "** instance id missing **")

    def test_count(self):
        """
        Test the 'count' command of the console.
        Checks if the command prints a valid count of instances.
        """
        with patch('sys.stdout', new=StringIO) as mock_stdout:
            self.console.onecmd("count BaseModel")
            output = mock_stdout.getvalue().strip()
            self.assertTrue(output.isdigit())


if __name__ == '__main__':
    unittest.main()
