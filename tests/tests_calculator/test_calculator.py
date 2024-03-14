# pylint: disable = expression-not-assigned
# pylint: disable = too-many-arguments
# pylint: disable = unused-argument

'''Test Calculator'''
import pytest
from app.calculator import Calculator

class TestCalculator():
    '''Tests Calculator.Operations'''

    def test_calculator_execute_faker(self, a, b, operation, expected):
        '''Tests Calculator.execute with Faker'''
        assert Calculator.execute(a, b, operation) == expected, f"{operation.__name__} operation failed!"

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

    @pytest.mark.parametrize("a_string, b_string, operation_string, expected_string", [
        ("5", "3", "add", "The result of 5 add 3 is equal to 8."),
        ("5", "3", "subtract", "The result of 5 subtract 3 is equal to 2."),
        ("5", "3", "multiply",  "The result of 5 multiply 3 is equal to 15."),
        ("6", "3", "divide", "The result of 6 divide 3 is equal to 2."),
        ("5", "0", "divide", "An error occurred: Cannot divide by zero."),
        ("5", "3", "unknown", "Unknown operation: unknown."),
        ("a", "3", "add", "Invalid number input: a or 3 is not a valid number."),
        ("3", "a", "add", 'Invalid number input: 3 or a is not a valid number.')
    ])

    def test_calculate_and_print(self, a_string, b_string, operation_string, expected_string, capsys):
        '''Tests Calculator.calculate_and_print'''
        Calculator.calculate_and_print(a_string, b_string, operation_string)
        captured = capsys.readouterr()
        assert captured.out.strip() == expected_string, "Calculator Calculate and Print failed!"
