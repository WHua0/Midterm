'''Test History'''
import unittest
import pandas as pd
from app.calculator.history import History
from app.calculator.operations import Operation

class TestHistory(unittest.TestCase):
    '''Tests History'''
    def setUp(self):
        self.history = History()
        self.history.history = pd.DataFrame()

    def test_create_log(self):
        '''Tests History.create_log'''
        log = self.history.create_log(10, 5, Operation.add)
        expected_log = {"Operation": "add", "OperandA": 10, "OperandB": 5}
        self.assertEqual(log, expected_log)

    def test_add_log(self):
        '''Tests History.add_log'''
        self.assertEqual(len(self.history.history), 0)
        log = {"add", 10, 5}
        self.history.add_log(log)
        self.assertEqual(len(self.history.history), 1)

    def test_get_history(self):
        '''Tests History.get_history'''
        self.assertEqual(len(self.history.history), 0)
        log = {"Operation": "add", "OperandA": 10, "OperandB": 5}
        self.history.add_log(log)
        self.assertIsInstance(self.history.get_history(), pd.DataFrame)

    def test_clear_history(self):
        '''Tests History.clear_history'''
        log = {"Operation": "add", "OperandA": 10, "OperandB": 5}
        self.history.add_log(log)
        self.assertEqual(len(self.history.history), 1)
        self.history.clear_history()
        self.assertEqual(len(self.history.history), 0)

    def test_delete_log(self):
        '''Tests History.delete_log'''
        log = {"Operation": "add", "OperandA": 10, "OperandB": 5}
        self.history.add_log(log)
        self.history.add_log(log)
        self.assertEqual(len(self.history.history), 2)
        self.history.delete_log(0)
        self.assertEqual(len(self.history.history), 1)

if __name__ == '__main__':
    unittest.main() # pragma: no cover
