'''Test HistoryHandler'''
import unittest
from app.calculator.history import History
from app.historyhandler import HistoryHandler

class TestHistoryHandler(unittest.TestCase):
    '''Tests HistoryHandler'''

    def test_create_history(self):
        '''Tests HistoryHandler.create_history'''
        expected_history_instance = History()
        actual_history_instance = HistoryHandler.create_history()
        self.assertIs(expected_history_instance, actual_history_instance)

    def test_retrieve_history(self):
        '''Tests HistoryHandler.retrieve_history'''
        history_instance = History()
        log = {"Operation": "add", "OperandA": 1, "OperandB": 1}
        history_instance.add_log(log)
        expected_history = str(history_instance.get_history())
        actual_history = str(HistoryHandler.retrieve_history(history_instance))
        self.assertEqual(expected_history, actual_history)

    def test_clear_history(self):
        '''Tests HistoryHandler.clear_history'''
        history_instance = History()
        log = {"Operation": "add", "OperandA": 1, "OperandB": 1}
        history_instance.add_log(log)
        HistoryHandler.clear_history(history_instance)
        self.assertTrue(history_instance.get_history().empty)

if __name__ == '__main__':
    unittest.main() # pragma: no cover
