# pylint: disable = unused-argument
# pylint: disable = duplicate-code

'''Test Add'''
import unittest
from unittest.mock import patch
from app.plugins.add import AddCommand

class TestAddCommand(unittest.TestCase):
    '''Tests AddCommand'''

    @patch("builtins.input", side_effect=["3 5"])
    def test_execute_with_correct_inputs(self, mock_input):
        '''Tests Execute_AddCommand with Correct Number of Inputs'''
        command = AddCommand()
        with patch("builtins.print") as mock_print:
            command.execute()
        mock_print.assert_called_once_with("The result of 3 add 5 is equal to 8.")

    @patch("builtins.input", side_effect=["3"])
    def test_execute_with_incorrect_inputs(self, mock_input):
        '''Tests Execute_AddCommand with Incorrect Number of Inputs'''
        command = AddCommand()
        with patch("builtins.print") as mock_print:
            command.execute()
        mock_print.assert_called_once_with("An error occurred: incorrect number of inputs.")

if __name__ == '__main__':
    unittest.main() # pragma: no cover
