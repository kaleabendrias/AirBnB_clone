#!/usr/bin/python3

"""
this is a test module for the console
"""
import unittest
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand


class TestConsole(unittest.TestCase):
    """Test cases for the console.py"""
    def test_help(self):
        """Test the help command"""
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            with patch('sys.stdin', StringIO("help\nquit\n")):
                HBNBCommand().cmdloop()
            output = mock_stdout.getvalue().strip()
            self.assertIn("Documented commands (type help <topic>):", output)
            self.assertIn("quit  --- Quit the console", output)

    def test_create(self):
        """Test the create command"""
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            with patch('sys.stdin', StringIO("create BaseModel\nall\n")):
                HBNBCommand().cmdloop()
            output = mock_stdout.getvalue().strip()
            self.assertIn("BaseModel", output)

    def test_show(self):
        """Test the show command"""
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            with patch('sys.stdin', StringIO("create BaseModel\nshow BaseModel\n")):
                HBNBCommand().cmdloop()
            output = mock_stdout.getvalue().strip()
            self.assertIn("BaseModel", output)

    def test_destroy(self):
        """Test the destroy command"""
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            with patch('sys.stdin', StringIO("create BaseModel\ndestroy BaseModel\n")):
                HBNBCommand().cmdloop()
            output = mock_stdout.getvalue().strip()
            self.assertEqual(output, "")
