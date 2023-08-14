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
            self.console.onecmd("BaseModel.count")
            self.assertIn("", mock_stdout.getvalue())
            
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
    
    def test_help_create(self):
        """ Test help_create method"""
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("help create")
            output = f.getvalue().strip()
            self.assertIsNotNone(output)
    
    def test_help_show(self):
        """ Test help_show method"""
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("help show")
            output = f.getvalue().strip()
            self.assertIsNotNone(output)
    
    def test_help_destroy(self):
        """ Test help_destroy method"""
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("help destroy")
            output = f.getvalue().strip()
            self.assertIsNotNone(output)
    
    def test_help_all(self):
        """ Test help_all method"""
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("help all")
            output = f.getvalue().strip()
            self.assertIsNotNone(output)

    def test_help_update(self):
        """ Test help_update method"""
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("help update")
            output = f.getvalue().strip()
            self.assertIsNotNone(output)
            
    def test_create_with_valid_class_name_BaseModel(self):
        """ Test create with valid class name"""
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("create BaseModel")
            output = f.getvalue().strip()
            try:
                uuid.UUID(output)
            except ValueError:
                self.fail("Output is not a valid UUID")

    def test_create_with_valid_class_name_User(self):
        """ Test create with valid class name"""
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("create User")
            output = f.getvalue().strip()
            try:
                uuid.UUID(output)
            except ValueError:
                self.fail("Output is not a valid UUID")

    def test_create_with_valid_class_name_Place(self):
        """ Test create with valid class name"""
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("create Place")
            output = f.getvalue().strip()
            try:
                uuid.UUID(output)
            except ValueError:
                self.fail("Output is not a valid UUID")

    def test_create_with_valid_class_name_State(self):
        """ Test create with valid class name"""
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("create State")
            output = f.getvalue().strip()
            try:
                uuid.UUID(output)
            except ValueError:
                self.fail("Output is not a valid UUID")

    def test_create_with_valid_class_name_City(self):
        """ Test create with valid class name"""
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("create City")
            output = f.getvalue().strip()
            try:
                uuid.UUID(output)
            except ValueError:
                self.fail("Output is not a valid UUID")

    def test_create_with_valid_class_name_Amenity(self):
        """ Test create with valid class name"""
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("create Amenity")
            output = f.getvalue().strip()
            try:
                uuid.UUID(output)
            except ValueError:
                self.fail("Output is not a valid UUID")

    def test_create_with_valid_class_name_Review(self):
        """ Test create with valid class name"""
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("create Review")
            output = f.getvalue().strip()
            try:
                uuid.UUID(output)
            except ValueError:
                self.fail("Output is not a valid UUID")
    
    def test_create_without_class_name(self):
        """ Test create without class name"""
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("create")
            output = f.getvalue().strip()
            self.assertEqual(output, "** class name missing **")
    
    def test_create_with_invalid_class_name(self):
        """ Test create with invalid class name"""
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("create MyModel")
            output = f.getvalue().strip()
            self.assertEqual(output, "** class doesn't exist **")

    def test_show_with_valid_class_and_id(self):
        """ Test show with valid class and id"""
        test_inst = User()
        test_inst.save()
        cmd = f"show User {test_inst.id}"
        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd(cmd)
            output = f.getvalue().strip()
            self.assertIn(f"[User] ({test_inst.id})", output)
            self.assertIn("created_at", output)
            self.assertIn("updated_at", output)
            self.assertIn("id", output)
            self.assertNotIn("__class__", output)
            self.assertFalse(output.startswith('["'))
            self.assertFalse(output.endswith('"]'))

    

if __name__ == '__main__':
    unittest.main()
