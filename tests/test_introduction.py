# pylint: disable = unused-import

'''Test Introduction'''
import pytest
from app.introduction import introduction

class TestIntroduction():
    '''Tests Introduction'''

    def test_introduction(self, capsys):
        '''Tests Introduction'''
        introduction()
        captured = capsys.readouterr()
        result = "Calculator App Initiated ...\nPlease type a command.\n"
        assert captured.out == result, "Introduction Function failed!"
