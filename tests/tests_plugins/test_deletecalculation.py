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
        initial_data = {"0": ["add", 10, 5]}
        df = pd.DataFrame(initial_data, index = ["Operation", "OperandA", "OperandB"])
        delete_calculation = DeleteCalculationCommand()
        delete_calculation.execute()
        self.assertListEqual(list(df.columns), ["0"])

    @patch("builtins.input", return_value = "100")
    @patch("logging.warning")
    def test_execute_invalid_index(self, mock_logging_warning, mock_input):
        '''Tests Excute_DeleteCalculation with Invalid Index'''
        delete_calculation = DeleteCalculationCommand()
        delete_calculation.execute()
        mock_logging_warning.assert_called_with("Index out of range, User inputted 100, Failed to delete calculation.")

    @patch("builtins.input", return_value = "abc")
    @patch("logging.warning")
    def test_execute_valueerror(self, mock_logging_warning, mock_input):
        '''Tests Excute_DeleteCalculation with Value Error'''
        delete_calculation = DeleteCalculationCommand()
        delete_calculation.execute()
        mock_logging_warning.assert_called_with("ValueError, User inputted abc, Failed to delete calculation.")

if __name__ == '__main__':
    unittest.main() # pragma: no cover
