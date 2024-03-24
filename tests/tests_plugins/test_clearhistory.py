'''Test ClearHistory'''
import unittest
from unittest.mock import patch
from app.plugins.clearhistory import ClearHistoryCommand

class TestClearHistoryCommand(unittest.TestCase):
    '''Tests ClearHistoryCommand'''

    @patch("app.plugins.clearhistory.HistoryHandler")
    @patch("app.plugins.clearhistory.logging")
    def test_execute(self, mock_logging, mockhistoryhandler):
        '''Tests Execute_ClearHistory'''
        history_data = []
        mockhistoryhandler.return_value.retrieve_history.return_value = history_data
        command = ClearHistoryCommand()
        command.execute()
        mock_logging.info.assert_called_once_with("Cleared history\nEmpty DataFrame\nColumns: []\nIndex: [].")
