# pylint: disable = expression-not-assigned

'''Test Calculation'''
import pytest
from app.calculator.calculation import Calculation
from app.calculator.operations import Operation

class TestCalculation():
    '''Tests Calculations.Compute with Operations'''

    def test_calculation_faker(self, a, b, operation, expected):
        '''Tests Calculation.Compute with Faker'''
        calc = Calculation(a, b, operation)
        assert calc.compute() == expected, "Calculation Compute with Faker failed!"

    def test_calculation_add(self):
        '''Tests with add'''
        calc = Calculation(2, 2, Operation.add)
        assert calc.compute() == 4, "Calculation Compute Add failed!"

    def test_calculation_subtract(self):
        '''Tests with subtract'''
        calc = Calculation(2, 2, Operation.subtract)
        assert calc.compute() == 0, "Calculation Compute Subtract failed!"

    def test_calculation_multiply(self):
        '''Tests with multiply'''
        calc = Calculation(2, 2, Operation.multiply)
        assert calc.compute() == 4, "Calculation Compute Multiply failed!"

    def test_calculation_divide(self):
        '''Tests with divide'''
        calc = Calculation(2, 2, Operation.divide)
        assert calc.compute() == 1, "Calculation Compute Divide failed!"

    def test_calculation_divide_by_zero(self):
        '''Tests with divide by 0 exception'''
        calc = Calculation(2, 0, Operation.divide)
        with pytest.raises(ZeroDivisionError, match = "Cannot divide by zero"):
            calc.compute(), "Calculation Compute ZeroDivisionError failed!"
