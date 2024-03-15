'''Test HistoryHandler'''
import os
import unittest
from app.calculator.history import History
from app.historyhandler import HistoryHandler

class TestHistoryHandler(unittest.TestCase):
    '''Tests HistoryHandler'''

    def setUp(self):
        self.history_instance = History()
        self.filenames = []

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

    def test_save_history(self):
        '''Tests HistoryHandler.save_history'''
        log = {"Operation": "add", "OperandA": 1, "OperandB": 1}
        self.history_instance.add_log(log)
        filename = "filename.csv"
        self.filenames.append(filename)
        HistoryHandler.save_history(self.history_instance, filename)
        self.assertTrue(os.path.isfile(filename))
        self.assertTrue(os.path.getsize(filename) > 0)

    def test_save_history_invalid_filename(self):
        '''Tests HistoryHandler.save_history'''
        log = {"Operation": "add", "OperandA": 1, "OperandB": 1}
        self.history_instance.add_log(log)
        filename = "$invalidfilename.csv"
        self.filenames.append(filename)
        HistoryHandler.save_history(self.history_instance, filename)
        with self.assertRaises(Exception):
            HistoryHandler.save_history(self.history_instance, filename)

    def tearDown(self):
        for filename in self.filenames:
            if os.path.exists(filename):
                os.remove(filename)

if __name__ == '__main__':
    unittest.main() # pragma: no cover
