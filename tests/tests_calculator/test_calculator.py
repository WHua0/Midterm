# pylint: disable = expression-not-assigned

'''Test Calculator'''
import pytest
from app.calculator import Calculator

class TestCalculator():
    '''Tests Calculator.Operations'''

    def test__execute_operations(self, a, b, operation, expected):
        '''Tests Calculator.execute with Faker'''
        assert Calculator.execute(a, b, operation) == expected, f"{operation.__name__} operation failed"

    def test_calculator_add(self):
        '''Tests Calculator.add'''
        assert Calculator.add(2, 2)  == 4, "Calculator Add failed!"

    def test_calculator_subtract(self):
        '''Tests Calculator.subtract'''
        assert Calculator.subtract(2, 2)  == 0, "Calculator Subtract failed!"

    def test_calculator_multiply(self):
        '''Tests Calculator.multiply'''
        assert Calculator.multiply(2, 2)  == 4, "Calculator Multiply failed!"

    def test_calculator_divide(self):
        '''Calculator.divide'''
        assert Calculator.divide(2, 2)  == 1, "Calculator Divide failed!"

    def test_calculator_division_by_zero(self):
        '''Calculator.add by 0 exception'''
        with pytest.raises(ZeroDivisionError, match = "Cannot divide by zero"):
            Calculator.divide(2, 0), "Calculator Divide ZeroDivisionError failed!"
