'''Test Menu'''
import sys
from io import StringIO
import unittest
from unittest.mock import MagicMock
from app.plugins.menu import MenuCommand

class TestMenuCommand(unittest.TestCase):
    '''Tests MenuCommand'''

    def test_execute(self):
        '''Tests Execute_MenuCommand'''

        command_handler_mock = MagicMock()
        command_handler_mock.commands = {
            "command1": MagicMock(),
            "command2": MagicMock()
        }
        menu_command = MenuCommand(command_handler_mock)
        saved_stdout = sys.stdout

        try:
            sys.stdout = StringIO()
            menu_command.execute()
            printed_output = sys.stdout.getvalue().strip()
            expected_output = "List of Commands:\ncommand1\ncommand2"
            self.assertEqual(printed_output, expected_output)

        finally:
            sys.stdout = saved_stdout

if __name__ == "__main__":
    unittest.main() # pragma: no cover
