import pandas as pd
from decimal import Decimal

class History:
    '''Singleton Class History'''

    _instance = None
    _columns = ["Operation", "OperandA", "OperandB"]

    def __new__(cls):
        '''Singleton Instance'''
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.history = pd.DataFrame(columns = cls._columns)
        return cls._instance

    def create_log(self, a: Decimal, b: Decimal, operation):
        '''Converts inputs to a log'''
        log = {"Operation": operation.__name__, "OperandA": a, "OperandB": b}
        return log

    def add_log(self, log):
        '''Adds log to history'''
        new_log = pd.DataFrame([log], columns = self._columns)
        self.history = pd.concat([self.history, new_log], ignore_index = True)

    def get_history(self):
        '''Returns history'''
        return self.history

    def clear_history(self):
        '''Clears history'''
        self.history = pd.DataFrame(columns = self._columns)

    def delete_log(self, index):
        '''Delete log at given index'''
        self.history = self.history.drop(index).reset_index(drop = True)
