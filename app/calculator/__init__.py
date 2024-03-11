'''Calculator Facade'''
from decimal import Decimal
from app.calculator.calculation import Calculation
from app.calculator.operations import Operation

class Calculator:
    '''Class Calculator'''

    @staticmethod
    def execute(a: Decimal, b: Decimal, operation) -> Decimal:
        '''Encaspulation with Calculator.execute '''
        calculation = Calculation(a, b, operation)
        return calculation.compute()

    @staticmethod
    def add(a: Decimal, b: Decimal) -> Decimal:
        '''Calculator.add(a, b)'''
        return Calculator.execute(a, b, Operation.add)

    @staticmethod
    def subtract(a: Decimal, b: Decimal) -> Decimal:
        '''Calculator.subtract(a, b)'''
        return Calculator.execute(a, b, Operation.subtract)

    @staticmethod
    def multiply(a: Decimal, b: Decimal) -> Decimal:
        ''''Calculator.multiply(a, b)'''
        return Calculator.execute(a, b, Operation.multiply)

    @staticmethod
    def divide(a: Decimal, b: Decimal) -> Decimal:
        '''Calculator.divide(a, b)'''
        return Calculator.execute(a, b, Operation.divide)
