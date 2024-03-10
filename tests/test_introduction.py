# pylint: disable = unused-import

'''Test Introduction'''
import pytest
from app.introduction import introduction

def test_introduction(capsys):
    '''Tests introduction'''
    introduction()
    captured = capsys.readouterr()
    result = "Calculator App Initiated ...\nPlease type a command.\n"
    assert captured.out == result, "Introduction Function failed!"
