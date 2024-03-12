# pylint: disable = redefined-outer-name
# pylint: disable = unused-argument

'''Test History'''
import pytest
from app.calculator.history import History
from app.calculator.operations import Operation

class TestHistory():
    '''Tests History'''

    @pytest.fixture
    def setup_history(self):
        '''Clears history and adds sample history for tests'''
        History.history.clear()
        log1 = ("add", 2, 2)
        log2 = ("subtract", 2, 2)
        History.history.append(log1)
        History.history.append(log2)

    def test_create_log(self):
        '''Tests create_log'''
        log = History.create_log(2, 2, Operation.add)
        assert log == ("add", 2, 2), "Failed to create log!"

    def test_add_log(self, setup_history):
        '''Tests add_log to history'''
        log3 = (2, 2, Operation.multiply)
        History.add_log(log3)
        assert len(History.history) == 3, "Failed to add log to history!"

    def test_retrieve_history(self, setup_history):
        '''Tests retrieve_history'''
        all_logs = History.retrieve_history()
        assert all_logs == History.history, "Failed to retrieve history!"

    def test_retrieve_no_history(self, setup_history):
        '''Tests retrieve_no_history'''
        History.history.clear()
        assert History.retrieve_history() == "No History!", "Failed to show no history!"

    def test_clear_history(self, setup_history):
        '''Tests clear history'''
        History.clear_history()
        assert len(History.history) == 0, "Failed to clear history!"

    def test_retrieve_previous_log(self, setup_history):
        '''Tests retrieve_previous_log from history'''
        assert History.retrieve_previous_log() == ("subtract", 2, 2), "Failed to retrieve previous log!"

    def test_retrieve_no_previous_log(self, setup_history):
        '''Tests retrieve_no_previous_log'''
        History.clear_history()
        assert History.retrieve_previous_log() == "No History!", "Failed to show no previous log!"
