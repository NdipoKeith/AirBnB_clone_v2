#!/usr/bin/python3
"""unittest for console.py"""
import unittest
from console import CommandInterpreter
import os
import mysql.connector


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
