'''Test Clear_History'''
import unittest
from unittest.mock import patch
from app.plugins.clear_history import ClearHistoryCommand
from app.calculator.history import History

class TestShowHistoryCommand():
    '''Tests ClearHistoryCommand'''

    def test_execute(self):
        '''Tests Execute_ClearHistoryCommand'''
        History.history.clear()
        log = ("add", 2, 2)
        History.add_log(log)
        command = ClearHistoryCommand()
        with patch("builtins.print"):
            command.execute()
        assert len(History.history) == 0

if __name__ == '__main__':
    unittest.main() # pragma: no cover
