import pandas as pd
from decimal import Decimal

class History:
    '''Singleton Class History'''

    _instance = None

    def __new__(cls):
        '''Singleton Instance'''
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.history = pd.DataFrame(columns=["Operation", "OperandA", "OperandB"])
        return cls._instance

    def create_log(self, a: Decimal, b: Decimal, operation):
        '''Converts inputs to a log'''
        log = {"Operation": operation.__name__, "OperandA": a, "OperandB": b}
        return log

    def add_log(self, log):
        '''Adds log to history'''
        new_log = pd.DataFrame([log], columns=["Operation", "OperandA", "OperandB"])
        self.history = pd.concat([self.history, new_log], ignore_index=True)

    def retrieve_history(self):
        '''Retrieves history'''
        if not self.history.empty:
            return self.history
        return None

    def clear_history(self):
        '''Clears history'''
        self.history = pd.DataFrame(columns=["Operation", "OperandA", "OperandB"])
