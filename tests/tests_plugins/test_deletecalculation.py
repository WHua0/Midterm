# pylint: disable = unused-argument
# pylint: disable = unused-import

'''Test DeleteCalculation'''
import unittest
import logging
from unittest.mock import patch
import pandas as pd
from app.plugins.deletecalculation import DeleteCalculationCommand

class TestDeleteCalculationCommand(unittest.TestCase):
    '''Tests DeleteCalculationCommand'''

    @patch("builtins.input", return_value = "0")
    @patch("logging.info")
    def test_execute(self, mock_logging_info, mock_input):
        '''Tests Excute_DeleteCalculation'''
        pd.DataFrame({"0": ["add", 10, 5]}, index = ["Operation", "OperandA", "OperandB"])
        delete_calculation = DeleteCalculationCommand()
        delete_calculation.execute()
        mock_logging_info.assert_called()

    @patch("builtins.input", return_value = "100")
    @patch("logging.info")
    def test_execute_invalid_index(self, mock_logging_info, mock_input):
        '''Tests Excute_DeleteCalculation with Invalid Index'''
        delete_calculation = DeleteCalculationCommand()
        delete_calculation.execute()
        mock_logging_info.assert_called_with("Index out of range: '100'.")

    @patch("builtins.input", return_value = "abc")
    @patch("logging.warning")
    def test_execute_valueerror(self, mock_logging_warning, mock_input):
        '''Tests Excute_DeleteCalculation with Value Error'''
        delete_calculation = DeleteCalculationCommand()
        delete_calculation.execute()
        mock_logging_warning.assert_called_with("Invalid Input: 'abc'.")


if __name__ == '__main__':
    unittest.main() # pragma: no cover
