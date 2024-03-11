# pylint: disable = unused-argument
# pylint: disable = expression-not-assigned

'''Test Operations'''
import pytest
from app.calculator.operations import Operation

class TestOperations():
    '''Tests Operations'''

    def test_add(self):
        '''Tests add'''
        assert Operation.add(2, 2) == 4, "Add failed!"

    def test_subtract(self):
        '''Tests subtract'''
        assert Operation.subtract(2, 2) == 0, "Subtract failed!"

    def test_multiply(self):
        '''Tests multiply'''
        assert Operation.multiply(2, 2) == 4, "Multiply failed!"

    def test_divide(self):
        '''Tests divide'''
        assert Operation.divide(2, 2) == 1, "Divide failed!"

    def test_divide_by_zero(self):
        '''Tests divide by 0 exception'''
        with pytest.raises(ZeroDivisionError, match = "Cannot divide by zero"):
            Operation.divide(2, 0), "ZeroDivisionError failed"
