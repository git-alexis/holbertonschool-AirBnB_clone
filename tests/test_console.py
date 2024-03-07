import unittest
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand
from models.engine.file_storage import FileStorage
from models import storage
from models.base_model import BaseModel


class TestConsole(unittest.TestCase):
    def setUp(self):
        self.console = HBNBCommand()

    def tearDown(self):
        self.console = None
        storage.reload()

    def test_create(self):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.console.onecmd("create BaseModel")
            output = mock_stdout.getvalue().strip()
            self.assertTrue(output)
            self.assertIn(output, storage.all())

    def test_show(self):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.console.onecmd("create BaseModel")
            output = mock_stdout.getvalue().strip()
            self.assertTrue(output)
            with patch('sys.stdout', new_callable=StringIO) as mock_stdout2:
                self.console.onecmd(f"show BaseModel {output}")
                show_output = mock_stdout2.getvalue().strip()
                self.assertIn("BaseModel", show_output)

    def test_destroy(self):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.console.onecmd("create BaseModel")
            output = mock_stdout.getvalue().strip()
            self.assertTrue(output)
            with patch('sys.stdout', new_callable=StringIO) as mock_stdout2:
                self.console.onecmd(f"destroy BaseModel {output}")
                destroy_output = mock_stdout2.getvalue().strip()
                self.assertFalse(destroy_output)
                self.assertNotIn(output, storage.all())

    def test_all(self):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.console.onecmd("all")
            all_output = mock_stdout.getvalue().strip()
            self.assertNotIn("BaseModel", all_output)
            self.console.onecmd("create BaseModel")
            self.console.onecmd("all")
            all_output = mock_stdout.getvalue().strip()
            self.assertIn("BaseModel", all_output)

    def test_update(self):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.console.onecmd("create BaseModel")
            output = mock_stdout.getvalue().strip()
            self.assertTrue(output)
            with patch('sys.stdout', new_callable=StringIO) as mock_stdout2:
                self.console.onecmd(f"update BaseModel {output} last_name 'John'")
                self.console.onecmd(f"show BaseModel {output}")
                show_output = mock_stdout2.getvalue().strip()
                self.assertIn("'last_name': 'John'", show_output)

    def test_create_syntax_error(self):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.console.onecmd("create")
            output = mock_stdout.getvalue().strip()
            self.assertEqual(output, "** class name missing **")

    def test_create_unknown_class(self):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.console.onecmd("create UnknownClassName")
            output = mock_stdout.getvalue().strip()
            self.assertEqual(output, "** class doesn't exist **")

    def test_show_syntax_error(self):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.console.onecmd("show")
            output = mock_stdout.getvalue().strip()
            self.assertEqual(output, "** class name missing **")

    def test_show_unknown_class(self):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.console.onecmd("show UnknownClassName")
            output = mock_stdout.getvalue().strip()
            self.assertEqual(output, "** class doesn't exist **")

    def test_show_no_id(self):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.console.onecmd("show BaseModel")
            output = mock_stdout.getvalue().strip()
            self.assertEqual(output, "** instance id missing **")

    def test_destroy_syntax_error(self):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.console.onecmd("destroy")
            output = mock_stdout.getvalue().strip()
            self.assertEqual(output, "** class name missing **")

    def test_destroy_unknown_class(self):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.console.onecmd("destroy UnknownClassName")
            output = mock_stdout.getvalue().strip()
            self.assertEqual(output, "** class doesn't exist **")

    def test_destroy_no_id(self):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.console.onecmd("destroy BaseModel")
            output = mock_stdout.getvalue().strip()
            self.assertEqual(output, "** instance id missing **")

    def test_all_syntax_error(self):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.console.onecmd("all UnknownClassName")
            output = mock_stdout.getvalue().strip()
            self.assertEqual(output, "** class doesn't exist **")

    def test_update_syntax_error(self):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.console.onecmd("update")
            output = mock_stdout.getvalue().strip()
            self.assertEqual(output, "** class name missing **")

    def test_update_unknown_class(self):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.console.onecmd("update UnknownClassName")
            output = mock_stdout.getvalue().strip()
            self.assertEqual(output, "** class doesn't exist **")

    def test_update_no_id(self):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.console.onecmd("update BaseModel")
            output = mock_stdout.getvalue().strip()
            self.assertEqual(output, "** instance id missing **")

    def test_update_no_attribute(self):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.console.onecmd("update BaseModel 1234")
            output = mock_stdout.getvalue().strip()
            self.assertEqual(output, "** attribute name missing **")

    def test_update_no_value(self):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.console.onecmd("update BaseModel 1234 first_name")
            output = mock_stdout.getvalue().strip()
            self.assertEqual(output, "** value missing **")


if __name__ == '__main__':
    unittest.main()
