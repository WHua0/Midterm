'''Test History Plugin'''
import unittest
import sys
from io import StringIO
from unittest.mock import MagicMock
from app.calculator.history import History
from app.plugins.history import ShowHistoryCommand

class TestShowHistoryCommand(unittest.TestCase):
    '''Tests ShowHistoryCommand'''

    def setUp(self):
        self.mock_history = MagicMock(spec = History)
        self.show_history_command = ShowHistoryCommand(self.mock_history)

    def test_execute(self):
        '''Tests Execute_History'''
        history_data = [
            {"Operation": "add", "OperandA": 1, "OperandB": 1},
        ]
        self.mock_history.retrieve_history.return_value = history_data
        captured_output = StringIO()
        sys.stdout = captured_output
        self.show_history_command.execute()
        sys.stdout = sys.__stdout__
        printed_output = captured_output.getvalue()
        expected_output = "History:\n  Operation  OperandA  OperandB\n0       add         1         1\n"
        self.assertEqual(printed_output, expected_output)

if __name__ == "__main__":
    unittest.main() # pragma: no cover
