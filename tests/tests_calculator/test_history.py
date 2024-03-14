'''Test History'''
import unittest
import pandas as pd
from app.calculator.history import History
from app.calculator.operations import Operation

class TestHistory(unittest.TestCase):
    '''Tests History'''
    def setUp(self):
        self.history = History()

    def test_create_log(self):
        '''Tests History.create_log'''
        log = self.history.create_log(10, 5, Operation.add)
        expected_log = {"Operation": "add", "OperandA": 10, "OperandB": 5}
        self.assertEqual(log, expected_log)

    def test_add_log(self):
        '''Tests History.add_log'''
        self.assertEqual(len(self.history.history), 0)
        log = self.history.create_log(10, 5, Operation.add)
        self.history.add_log(log)
        self.assertEqual(len(self.history.history), 1)

    def test_retrieve_no(self):
        '''Tests History.retrieve_history'''
        self.assertEqual(self.history.retrieve_history(), "No History!")

        log = {"Operation": "add", "OperandA": 10, "OperandB": 5}
        self.history.add_log(log)
        self.assertIsInstance(self.history.retrieve_history(), pd.DataFrame)

if __name__ == '__main__':
    unittest.main() # pragma: no cover
