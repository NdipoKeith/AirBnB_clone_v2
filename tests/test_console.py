#!/usr/bin/python3
"""
Contains the class TestConsoleDocs
"""
import os
import console
import inspect
import pep8
import unittest
import mysql.connector
from console import CommandInterpreter
HBNBCommand = console.HBNBCommand


class TestConsoleDocs(unittest.TestCase):
    """Class for testing documentation of the console"""
    def test_pep8_conformance_console(self):
        """Test that console.py conforms to PEP8."""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['console.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_pep8_conformance_test_console(self):
        """Test that tests/test_console.py conforms to PEP8."""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['tests/test_console.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_console_module_docstring(self):
        """Test for the console.py module docstring"""
        self.assertIsNot(console.__doc__, None,
                         "console.py needs a docstring")
        self.assertTrue(len(console.__doc__) >= 1,
                        "console.py needs a docstring")

    def test_HBNBCommand_class_docstring(self):
        """Test for the HBNBCommand class docstring"""
        self.assertIsNot(HBNBCommand.__doc__, None,
                         "HBNBCommand class needs a docstring")
        self.assertTrue(len(HBNBCommand.__doc__) >= 1,
                        "HBNBCommand class needs a docstring")


class Create_State(unittest.TestCase):
    """Test case to validate if the State created
    adds a new record in the db"""
    def set_up(self):
        self.conn = mysql.connector.connect(
                user="hbnb_test"
                passwd="hbnb_test_pwd"
                host="localhost"
                database="hbnb_env_db"
                )
        self.cursor = self.conn.cursor()

    def test_create_state(state):
        """tests to create state"""
        initial_count = self.get_record_count()
        command = ("create State name =\"California\"")
        result = self.interpreter.do_create(command)
        self.assertEqual((result-initial_count), 1)

    def test_get_record_count(self):
        """test to get the number of count after creating state in db states"""
        self.cursor.execute("SELECT COUNT(*) FROM states")
        result = self.cursor.fetchone()[0]
        return result

    def test_execute_command(self, command):
        """test with eample of executing a command in console"""
        pass

    def tearDown(self):
        """teardown the class"""
        self.cursor.close()
        self.conn.clode()


class CommandInterpreter(unittest.TestCase):

    def setUp(self):
        """setup class"""
        self.interpreter = commandInterpreter()

    def test_create_with_valid_str(self):
        """create object with valid string"""
        command = "create MyObj name = \"Tiny House\""
        result = self.interpreter.do_create(command)
        sel.assertEqual(result, "MyObj(name='Tiny House')")

    def test_create_with_valid_float(self):
        """creating object with a valid float number"""
        command = "create MyObj value = 5.678"
        result = self.interpreter.do_create(command)
        self.assertEqual(result, "MyObj(value = 5.678)")

    def test_create_obj_with_valid_int(self):
        """create object with a valid integer"""
        command = "create MyObj value = 15"
        result = self.interpreter.do_create(command)
        self.assertEqual(result, "MYObj(value = 15)")

    def test_create_obj_with_invalid_parameter(self):
        """test create object with invalid input parameter"""
        command = "create MyObj name = invalid_input"
        resul = self.interpreter.do_create(command)
        self.assertEqual(result, "Invalid parameter format")

    def test_create_command_with_invalid_parameter_name(self):
        """test command input with onvalid parameter name"""
        command = "create MyObj unknown_value=valid_value"
        result = self.interpreter.do_create(command)
        self.assertEqual(result, "unrecognized parameter name")

    def test_help_update_prints_correct_output(self):
        """test that the output prints the correct output"""
        expected_output_message = "Updates an object with new information"
        help_update()
        self.assertEqual(captured_output, expected_output_message)

    def test_help_for_all(self):
        """tets for correct output for help"""
        expected_output = "shows all objects, or all class"
        help_all()
        self.assertEqual(captured_output, expected_output)


class DoAllTests(unittest.TestCase):

    def test_do_all_no_args(self):
        """unittest for do_all, no args, ie, shows previous command"""
        args = ""
        expected_output = ["[User, id=100, email=dave@example.com, name=Dave]"]
        result = HNBCommand.do_all(self, args)
        self.assertEqual(result, expected_output)

    def test_if_valid_class_name(self):
        """unittest for valid name"""
        args = "User"
        expected_output = ["[User, id=125, email=dave@example.com, name=Dave]"]
        result = HBNBCommand do_all(self, args)
        self.assertEqual(result, expected_output)

    def test_invalid_class_name_input(self):
        """unittest for invalid class name"""
        args = "INvalidClass"
        expected_output = "** Class doesn't exist **"
        result = HBNBCommand do_all(self, args)
        self.assertEqual(result, expected_output)

    def test_help_create(self):
        """test help_create outputs the correct output"""
        expected_output = "Create a class of any type"
        help_create()
        self.assertEqual(captured_value, expected_output)

    def test_teardown(self):
        """teardown the class"""
        pass


if __name__ == "__main":
    unittest.main()
