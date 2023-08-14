from io import StringIO
from unittest.mock import patch
import unittest
from console import HBNBCommand
import os
from models.engine.file_storage import FileStorage
import console
import uuid
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class TestConsole(unittest.TestCase):
    """ test module for console"""

    def setUp(self):
        """ Create file at the beginning of every test"""
        try:
            os.remove("file.json")
        except IOError:
            pass
        FileStorage._FileStorage__objects = {}

    def tearDown(self):
        """ Delete created file after every test"""
        try:
            os.remove("file.json")
        except IOError:
            pass

    def test_module_doc(self):
        """ Test for module documentation"""
        self.assertIsNotNone(console.__doc__)

    def setUp(self):
        self.console = HBNBCommand()

    def test_quit(self):
        """ Test quit method"""
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("quit")
            output = f.getvalue().strip()
            self.assertEqual(output, "")

    def test_count(self):
        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            self.console.onecmd("count BaseModel")
            output = mock_stdout.getvalue().strip()
            self.assertTrue(output.isdigit())

    def test_EOF(self):
        """ Test EOF method"""
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("EOF")
            output = f.getvalue().strip()
            self.assertEqual(output, "")

    def test_empty_line(self):
        """ Test empty_line method"""
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("")
            output = f.getvalue().strip()
            self.assertEqual(output, "")

    def test_user_all(self):
        test_inst1 = User()
        test_inst1.save()
        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            self.console.onecmd("User.all()")
            output = mock_stdout.getvalue().strip()
            expected_output = f"[User] ({test_inst1.id})\n"
            self.assertIn(f"[User] ({test_inst1.id})", output)


if __name__ == '__main__':
    unittest.main()
