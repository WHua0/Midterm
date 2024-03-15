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

if __name__ == '__main__':
    unittest.main() # pragma: no cover
