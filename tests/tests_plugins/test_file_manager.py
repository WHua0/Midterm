# pylint: disable = unused-argument
# pylint: disable = unused-variable

'''Test Add'''
import unittest
from unittest.mock import patch
from app.plugins.file_manager import CSVCommand

class TestCSVCommand(unittest.TestCase):
    '''Tests File Manager: CSVCommand'''

    @patch("builtins.input", side_effect=["3 5"])
    @patch("logging.warning")
    def test_execute_with_correct_number_of_inputs(self, mock_logging_warning, mock_input):
        '''Tests Execute_CSVCommand with Correct Number of Inputs'''
        command = CSVCommand()
        with patch("builtins.print") as mock_print:
            command.execute()
            mock_logging_warning.assert_called_once_with("Invalid CSV Operation: 3.")

    @patch("builtins.input", side_effect=["3"])
    @patch("logging.warning")
    def test_execute_with_incorrect_number_of_inputs(self, mock_logging_warning, mock_input):
        '''Tests Execute_CSVCommand with Incorrect Number of Inputs'''
        command = CSVCommand()
        with patch("builtins.print") as mock_print:
            command.execute()
            mock_logging_warning.assert_called_once_with("Incorrect number of inputs: '%s'.", "3")

if __name__ == '__main__':
    unittest.main() # pragma: no cover
