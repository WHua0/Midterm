'''Encapsulates a Calculation'''
from decimal import Decimal

class Calculation:
    '''Class Calculation'''

    def __init__(self, a: Decimal, b: Decimal, operation):
        '''Encapsulates a single calculation'''

        self.a = a
        self.b = b
        self.operation = operation

    def compute(self):
        '''Executes the operation and returns the result'''
        return self.operation(self.a, self.b)
