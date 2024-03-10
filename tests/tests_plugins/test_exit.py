# pylint: disable = unused-variable

'''Exit Test'''
import sys
import pytest
from app.plugins import ExitCommand

class TestExitCommand:
    '''Tests ExitCommand'''

    @pytest.fixture
    def exit_command(self):
        '''Defines Fixture'''
        return ExitCommand()

    def test_execute(self, exit_command, monkeypatch):
        '''Tests Execute_ExitCommand'''
        exit_msg = None

        def mock_exit(msg):
            nonlocal exit_msg
            exit_msg = msg
            raise SystemExit

        monkeypatch.setattr(sys, "exit", mock_exit)
        with pytest.raises(SystemExit) as exc_info:
            exit_command.execute()
