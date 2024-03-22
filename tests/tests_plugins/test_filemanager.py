# pylint: disable = unused-argument
# pylint: disable = unused-variable

'''Test FileManager'''
import unittest
from unittest.mock import patch
from app.plugins.filemanager import FileManagerCommand

class TestFileCommand(unittest.TestCase):
    '''Tests FileManager Command'''

    @patch("builtins.input", side_effect=["3 5"])
    @patch("logging.warning")
    def test_execute_with_correct_number_of_inputs(self, mock_logging_warning, mock_input):
        '''Tests Execute_CSVCommand with Correct Number of Inputs'''
        command = FileManagerCommand()
        with patch("builtins.print") as mock_print:
            command.execute()
            mock_logging_warning.assert_called_once_with("Invalid File Operation: 3.")

    @patch("builtins.input", side_effect=["3"])
    @patch("logging.warning")
    def test_execute_with_incorrect_number_of_inputs(self, mock_logging_warning, mock_input):
        '''Tests Execute_CSVCommand with Incorrect Number of Inputs'''
        command = FileManagerCommand()
        with patch("builtins.print") as mock_print:
            command.execute()
            mock_logging_warning.assert_called_once_with("Incorrect number of inputs, User inputted 3, Failed to execute.")

if __name__ == '__main__':
    unittest.main() # pragma: no cover
