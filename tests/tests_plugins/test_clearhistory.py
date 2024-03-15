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
        command = ClearHistoryCommand()
        command.execute()
        mock_logging.info.assert_called_once_with("Cleared History.")
        mockhistoryhandler.return_value.clear_history.assert_called_once()
