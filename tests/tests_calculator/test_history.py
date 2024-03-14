'''Test History'''
import unittest
from app.calculator.history import History

class TestHistory(unittest.TestCase):
    '''Tests History'''
    def setUp(self):
        self.history = History()

    def test_create_log(self):
        '''Tests History.create_log'''
        log = self.history.create_log(10, 5, "add")
        expected_log = {"Operation": "add", "OperandA": 10, "OperandB": 5}
        self.assertEqual(log, expected_log)

if __name__ == '__main__':
    unittest.main() # pragma: no cover
