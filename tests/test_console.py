#!/usr/bin/python3
"""unittest console"""
import unittest
import console
import sys
import json
from unittest.mock import patch
import inspect
import pep8
from console import HBNBCommand
from models.amenity import Amenity
from models.city import City
from models.state import State
from models.base_model import BaseModel
from models.place import Place
from models.review import Review
from models.user import User
from models import storage


class TestConsole(unittest.TestCase):
    """Unittest for the console"""

    @classmethod
    def setUpClass(cls):
        """setup for the test"""
        cls.consol = HBNBCommand()

    @classmethod
    def teardown(cls):
        del cls.consol

    def tearDown(self):
        try:
            os.remove("file.json")
        except Exception:
            pass

    def test_pep8_console(self):
        """Test console conforms to PEP8"""
        style = pep8.StyleGuide(quiet=True)
        r = style.check_files(["console.py"])
        self.assertEqual(r.total_errors, 0, 'code style errors found.fix PEP8')

    def test_HBNBCommand_class_docstring(self):
        """Test for the HBNBCommand class docstring"""
        self.assertIsNotNone(console.__doc__)
        self.assertIsNotNone(HBNBCommand.emptyline.__doc__)
        self.assertIsNotNone(HBNBCommand.do_quit.__doc__)
        self.assertIsNotNone(HBNBCommand.do_EOF.__doc__)
        self.assertIsNotNone(HBNBCommand.do_create.__doc__)
        self.assertIsNotNone(HBNBCommand.do_show.__doc__)
        self.assertIsNotNone(HBNBCommand.do_destroy.__doc__)
        self.assertIsNotNone(HBNBCommand.do_all.__doc__)
        self.assertIsNotNone(HBNBCommand.do_update.__doc__)
        self.assertIsNotNone(HBNBCommand.count.__doc__)

    def test_help(self):
        """Test help command"""
        msg = """Documented commands (type help <topic>):
              ========================================
              EOF  all  count  create  destroy  help  quit  show  update
              """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help")
            self.assertEqual(msg, f.getvalue())

    def test_quit(self):
        """test quit command"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.consol.onecmd("quit")
            self.assertEqual('', f.getvalue())

    def test_emptyline(self):
        """test empty line"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.consol.onecmd("\n")
            self.assertEqual('', f.getvalue())

    def test_create(self):
        """test create command"""
        msg = "** class name missing **\n"
        with patch('sys.stdout', new=StringIO()) as f:
            self.consol.onecmd("create")
            self.assertEqual(msg, f.getvalue())

        msg = "** class doesn't exist **\n"
        with patch('sys.stdout', new=StringIO()) as f:
            self.consol.onecmd("create abcdef")
            self.assertEqual(msg, f.getvalue())

        with patch('sys.stdout', new=StringIO()) as f:
            self.consol.onecmd('create User email="abc@g.com" password="abcd"')
        with patch('sys.stdout', new=StringIO()) as f:
            self.consol.onecmd("all User")
            self.assertEqual("[[User]", f.getvalue()[:7])

    def test_show(self):
        """test show command"""
        msg = "** class name missing **\n"
        with patch('sys.stdout', new=StringIO()) as f:
            self.consol.onecmd("show")
            self.assertEqual(msg, f.getvalue())

        msg = "** class doesn't exist **\n"
        with patch('sys.stdout', new=StringIO()) as f:
            self.consol.onecmd("show abcdef")
            self.assertEqual(msg, f.getvalue())

        msg = "** instance id missing **\n"
        with patch('sys.stdout', new=StringIO()) as f:
            self.consol.onecmd("show BaseModel")
            self.assertEqual(msg, f.getvalue())

        msg = "** no instance found **\n"
        with patch('sys.stdout', new=StringIO()) as f:
            self.consol.onecmd("show BaseModel abcd-123")
            self.assertEqual(msg, f.getvalue())

    def test_destroy(self):
        """test destroy command"""
        msg = "** class name missing **\n"
        with patch('sys.stdout', new=StringIO()) as f:
            self.consol.onecmd("destroy")
            self.assertEqual(msg, f.getvalue())

        msg = "** class doesn't exist **\n"
        with patch('sys.stdout', new=StringIO()) as f:
            self.consol.onecmd("destroy abcdef")
            self.assertEqual(msg, f.getvalue())

        msg = "** instance id missing **\n"
        with patch('sys.stdout', new=StringIO()) as f:
            self.consol.onecmd("destroy User")
            self.assertEqual(msg, f.getvalue())

        msg = "** no instance found **\n"
        with patch('sys.stdout', new=StringIO()) as f:
            self.consol.onecmd("destroy BaseModel abcdef")
            self.assertEqual(msg, f.getvalue())

    def test_all(self):
        """test all command"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.consol.onecmd("all abcdef")
            self.assertEqual("** class doesn't exist **\n", f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            self.consol.onecmd("all State")
            self.assertEqual("[]\n", f.getvalue())

    def test_update(self):
        """test update command"""
        msg = "** class name missing **\n"
        with patch('sys.stdout', new=StringIO()) as f:
            self.consol.onecmd("update")
            self.assertEqual(msg, f.getvalue())

        msg = "** class doesn't exist **\n"
        with patch('sys.stdout', new=StringIO()) as f:
            self.consol.onecmd("update abcdef")
            self.assertEqual(msg, f.getvalue())


if __name__ == "__main__":
    unittest.main()
