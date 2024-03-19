'''Test HistoryHandler'''
import unittest
import pandas as pd
from app.calculator.history import History
from app.historyhandler import HistoryHandler

class TestHistoryHandler(unittest.TestCase):
    '''Tests HistoryHandler'''

    def setUp(self):
        self.history_instance = History()

    def test_create_history(self):
        '''Tests HistoryHandler.create_history'''
        expected_history_instance = History()
        actual_history_instance = HistoryHandler.create_history()
        self.assertIs(expected_history_instance, actual_history_instance)

    def test_retrieve_history(self):
        '''Tests HistoryHandler.retrieve_history'''
        log = {"Operation": "add", "OperandA": 1, "OperandB": 1}
        self.history_instance.add_log(log)
        expected_history = str(self.history_instance.get_history())
        actual_history = str(HistoryHandler.retrieve_history(self.history_instance))
        self.assertEqual(expected_history, actual_history)

    def test_clear_history(self):
        '''Tests HistoryHandler.clear_history'''
        log = {"Operation": "add", "OperandA": 1, "OperandB": 1}
        self.history_instance.add_log(log)
        HistoryHandler.clear_history(self.history_instance)
        self.assertTrue(self.history_instance.get_history().empty)

    def test_import_history(self):
        '''Tests HistoryHandler.import_history'''
        history_df = pd.DataFrame({"Operation": ["add"], "OperandA": [1], "OperandB": [1]})
        history_instance = HistoryHandler.import_history(history_df)
        self.assertEqual(history_df.to_dict(), history_instance.get_history().to_dict())

    def test_delete_calculation(self):
        '''Tests HistoryHandler.delete_calculation'''
        log1 = {"Operation": "add", "OperandA": 1, "OperandB": 1}
        log2 = {"Operation": "add", "OperandA": 2, "OperandB": 2}
        self.history_instance.add_log(log1)
        expected_history = str(self.history_instance.get_history())
        self.history_instance.add_log(log2)
        HistoryHandler.delete_calculation(self.history_instance, 1)
        actual_history = str(HistoryHandler.retrieve_history(self.history_instance))
        self.assertEqual(expected_history, actual_history)


if __name__ == '__main__':
    unittest.main() # pragma: no cover
