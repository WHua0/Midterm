'''Calculator Facade'''
import logging
from decimal import Decimal, InvalidOperation
from app.calculator.calculation import Calculation
from app.calculator.operations import Operation
from app.calculator.history import History

class Calculator:
    '''Class Calculator'''

    history = History()

    @staticmethod
    def execute(a: Decimal, b: Decimal, operation) -> Decimal:
        '''Encapsulation with Calculator.execute(a, b, operation) '''
        calculation = Calculation(a, b, operation)
        log = Calculator.history.create_log(a, b, operation)
        Calculator.history.add_log(log)
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

    @staticmethod
    def calculate_and_print(a: Decimal, b: Decimal, operation_name):
        '''Calculates and prints result'''

        operation_mappings = {
                "add": Calculator.add,
                "subtract": Calculator.subtract,
                "multiply": Calculator.multiply,
                "divide": Calculator.divide
        }

        try:
            a_decimal, b_decimal = map(Decimal, [a, b])
            operation_function = operation_mappings.get(operation_name)      

            if operation_function:
                result = operation_function(a_decimal, b_decimal)
                print(f"The result of {a} {operation_name} {b} is equal to {result}.")
                logging.info(f"Computed {a} {operation_name} {b} is equal to {result}.")

            else:
                print(f"Unknown operation: {operation_name}.")
                logging.error(f"Unknown operation {operation_name}.")

        except InvalidOperation:
            print(f"Invalid number input: {a} or {b} is not a valid number.")
            logging.warning(f"Invalid input {a} or {b}, Failed to calculate and print.")

        except ZeroDivisionError:
            print(f"An error occurred: ZeroDivisionError.")
            logging.warning(f"ZeroDivisionError, Failed to calculate and print.")
