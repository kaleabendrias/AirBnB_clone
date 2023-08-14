#!/usr/bin/python3

"""
this is a module used to test the console
"""

import unittest
from unittest.mock import patch, Mock
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
        with patch('sys.stdout', new_callable=StringIO) as f:
            self.console.onecmd("create BaseModel")
            output = f.getvalue().strip()
            self.assertTrue(len(output) > 0)

    def test_show(self):
        """
        Test the 'show' command of the console.
        Checks if the command prints the correct
        message when instance ID is missing.
        """
        with patch('sys.stdout', new_callable=StringIO) as f:
            self.console.onecmd("show BaseModel")
            output = f.getvalue().strip()
            self.assertEqual(output, "** instance id missing **")

    def test_destroy(self):
        """
        Test the 'destroy' command of the console.
        Checks if the command prints the correct
        message when instance ID is missing.
        """
        with patch('sys.stdout', new_callable=StringIO) as f:
            self.console.onecmd("destroy BaseModel")
            output = f.getvalue().strip()
            self.assertEqual(output, "** instance id missing **")

    def test_all(self):
        """
        Test the 'all' command of the console.
        Checks if the command prints a list of all instances.
        """
        with patch('sys.stdout', new_callable=StringIO) as f:
            self.console.onecmd("all")
            output = f.getvalue().strip()
            self.assertTrue(len(output) > 0)

    def test_update(self):
        """
        Test the 'update' command of the console.
        Checks if the command prints the correct
        message when instance ID is missing.
        """
        with patch('sys.stdout', new_callable=StringIO) as f:
            self.console.onecmd("update BaseModel")
            output = f.getvalue().strip()
            self.assertEqual(output, "** instance id missing **")

    def test_count(self):
        """
        Test the 'count' command of the console.
        Checks if the command prints a valid count of instances.
        """
        with patch('sys.stdout', new_callable=StringIO) as f:
            self.console.onecmd("count BaseModel")
            output = f.getvalue().strip()
            self.assertTrue(output.isdigit())

    def test_quit(self):
        """
        test the 'quit' command of the console
        Checks if the command exits the console loop
        """
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("quit")
            self.assertEqual(f.getvalue(), "")

    def test_EOF(self):
        """
        test the 'EOF' command of the console
        Checks if the command exits the console loop
        """
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("EOF")
            self.assertEqual(f.getvalue(), "")

if __name__ == '__main__':
    unittest.main()
