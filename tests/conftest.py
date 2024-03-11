# pylint: disable = comparison-with-callable

'''conftest.py'''
from decimal import Decimal
from faker import Faker
from app.calculator.operations import Operation

fake = Faker()

operation_mapping = {
    "add": Operation.add,
    "subtract": Operation.subtract,
    "multiply": Operation.multiply,
    "divide": Operation.divide
}

def generate_test_data(number_of_records):
    '''Generates test data in the amount called'''

    for _ in range(number_of_records):
        a = Decimal(fake.random_number(digits = 2))
        b = Decimal(fake.random_number(digits = 2))
        operation_name = fake.random_element(elements = list(operation_mapping.keys()))
        operation_function = operation_mapping[operation_name]

        if operation_function == Operation.divide:
            b = Decimal("1") if b == Decimal("0") else b

        try:

            if operation_function == Operation.divide and b == Decimal("0"):
                expected = "ZeroDivisionError"

            else:
                expected = operation_function(a, b)

        except ZeroDivisionError:
            expected = "ZeroDivisionError"

        yield a, b, operation_name, operation_function, expected

def pytest_addoption(parser):
    '''Creates custom CLI option --num_records '''
    parser.addoption("--num_records", action = "store", default = 5, type = int, help = "Number of Test Records to Generate.")

def pytest_generate_tests(metafunc):
    '''Checks if the test is expecting any of the dynamically generated fixtures'''
    if {"a", "b", "expected"}.intersection(set(metafunc.fixturenames)):
        num_records = metafunc.config.getoption('num_records')
        parameters = list(generate_test_data(num_records))
        modified_parameters = [(a, b, op_name if "operation_name" in metafunc.fixturenames else op_func, expected) for a, b, op_name, op_func, expected in parameters]
        metafunc.parametrize("a, b, operation, expected", modified_parameters)
