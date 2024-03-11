# pylint: disable = unused-argument

'''Test Divide'''
import unittest
from unittest.mock import patch
from app.plugins.divide import DivideCommand

class TestDivideCommand(unittest.TestCase):
    '''Tests DivideCommand'''

    @patch("builtins.input", side_effect=["6 3"])
    def test_execute_with_correct_inputs(self, mock_input):
        '''Tests Execute_DivideCommand with Correct Number of Inputs'''
        command = DivideCommand()
        with patch("builtins.print") as mock_print:
            command.execute()
        mock_print.assert_called_once_with("The result of 6 divide 3 is equal to 2.")

    @patch("builtins.input", side_effect=["3"])
    def test_execute_with_incorrect_inputs(self, mock_input):
        '''Tests Execute_DivideCommand with Incorrect Number of Inputs'''
        command = DivideCommand()
        with patch("builtins.print") as mock_print:
            command.execute()
        mock_print.assert_called_once_with("An error occurred: incorrect number of inputs.")

if __name__ == '__main__':
    unittest.main() # pragma: no cover
