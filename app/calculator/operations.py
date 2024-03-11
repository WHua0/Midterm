'''Operations'''
from decimal import Decimal

class Operation:
    '''Class Operation'''

    @staticmethod
    def add(a: Decimal, b: Decimal) -> Decimal:
        '''Adds a and b'''
        return a + b

    @staticmethod
    def subtract(a: Decimal, b: Decimal) -> Decimal:
        '''Subtracts a and b'''
        return a - b

    @staticmethod
    def multiply(a: Decimal, b: Decimal) -> Decimal:
        '''Multiplies a and b'''
        return a * b

    @staticmethod
    def divide(a: Decimal, b: Decimal) -> Decimal:
        '''Divides a by b'''
        if b == 0:
            raise ZeroDivisionError("Cannot divide by zero")

        return a / b
