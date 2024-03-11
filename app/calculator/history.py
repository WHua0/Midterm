'''Manages History'''
from decimal import Decimal

class History:
    '''Class History'''

    history = []

    @classmethod
    def create_log(cls, a: Decimal, b: Decimal, operation):
        '''Converts inputs to a log'''
        cls.a = a
        cls.b = b
        cls.operation = operation.__name__
        return (cls.a, cls.b, cls.operation)

    @classmethod
    def add_log(cls, log):
        '''Adds log to history'''
        cls.history.append(log)

    @classmethod
    def retrieve_history(cls):
        '''Retrieves history'''
        if cls.history:
            return cls.history
        return "No History!"

    @classmethod
    def clear_history(cls):
        '''Clears history'''
        return cls.history.clear()

    @classmethod
    def retrieve_previous_log(cls):
        '''Retrieves previous log'''
        if cls.history:
            return cls.history[-1]
        return "No History!"
