'''Test Show_Previous'''
import unittest
from unittest.mock import patch
from app.plugins.show_previous import ShowPreviousCommand
from app.calculator.history import History

class TestShowPreviousCommand():
    '''Tests ShowPreviousCommand'''

    def test_execute_no_history(self):
        '''Tests Execute_ShowPrevious for No History'''
        History.history.clear()
        command = ShowPreviousCommand()
        with patch("builtins.print") as mock_print:
            command.execute()
        mock_print.assert_called_once_with("No History!")

    def test_execute(self):
        '''Tests Execute_ShowPreviousCommand'''
        History.history.clear()
        log = ("add", 2, 2)
        History.add_log(log)
        command = ShowPreviousCommand()
        with patch("builtins.print") as mock_print:
            command.execute()
        mock_print.assert_called_once_with(("add", 2, 2))

if __name__ == '__main__':
    unittest.main() # pragma: no cover
