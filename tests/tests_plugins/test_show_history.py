# pylint: disable = duplicate-code

'''Test Show_History'''
import unittest
from unittest.mock import patch
from app.plugins.show_history import ShowHistoryCommand
from app.calculator.history import History

class TestShowHistoryCommand():
    '''Tests ShowHistoryCommand'''

    def test_execute_no_history(self):
        '''Tests Execute_ShowHistoryCommand for No History'''
        History.history.clear()
        command = ShowHistoryCommand()
        with patch("builtins.print") as mock_print:
            command.execute()
        mock_print.assert_called_once_with("No History!")

    def test_execute(self):
        '''Tests Execute_ShowHistoryCommand'''
        History.history.clear()
        log = ("add", 2, 2)
        History.add_log(log)
        command = ShowHistoryCommand()
        with patch("builtins.print") as mock_print:
            command.execute()
        mock_print.assert_called_once_with([("add", 2, 2)])

if __name__ == '__main__':
    unittest.main() # pragma: no cover
