'''Test CommandHanager'''
import unittest
from unittest.mock import MagicMock
from app.commandhandler import Command, CommandHandler

class MockCommand(Command):
    '''Class MockCommand'''
    def execute(self):
        pass # pragma: no cover

class TestCommandManager(unittest.TestCase):
    '''Tests CommandManager'''

    def setUp(self):
        '''SetUp'''
        self.manager = CommandHandler()

    def test_register_command(self):
        '''Tests Register_Command'''
        command_name = "mock_command"
        command = MockCommand()
        self.manager.register_command(command_name, command)
        self.assertIn(command_name, self.manager.commands)
        self.assertEqual(self.manager.commands[command_name], command)

    def test_execute_command(self):
        '''Tests Execute_Valid_Command'''
        command_name = "mock_command"
        command = MockCommand()
        command.execute = MagicMock()
        self.manager.register_command(command_name, command)
        self.manager.execute_command(command_name)
        command.execute.assert_called_once()

    def test_execute_invalid_command(self):
        '''Tests Execute_Invalid_Command'''
        with unittest.mock.patch("builtins.print") as mocked_print:
            self.manager.execute_command("invalid_command")
            mocked_print.assert_called_with("Type 'exit' to exit.")

if __name__ == "__main__":
    unittest.main() # pragma: no cover
