'''Test ShowHistory'''
import unittest
from unittest.mock import patch
from app.plugins.showhistory import ShowHistoryCommand

class TestShowHistoryCommand(unittest.TestCase):
    '''Tests ShowHistoryCommand'''

    @patch("app.plugins.showhistory.HistoryHandler")
    @patch("app.plugins.showhistory.logging")
    def test_execute(self, mock_logging, mockhistoryhandler):
        '''Tests Execute_ShowHistory with empty history'''
        history_data = []
        mockhistoryhandler.return_value.retrieve_history.return_value = history_data
        command = ShowHistoryCommand()
        command.execute()
        mock_logging.info.assert_called_once_with("Printed history\nEmpty DataFrame\nColumns: []\nIndex: []")
