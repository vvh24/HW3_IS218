from faker import Faker

faker = Faker()
'''My Calculator Test'''
from calculator import Calculator

def test_operations(generate_test_data):
    for a, b, operation in generate_test_data:
        if operation == 'add':
            result = a + b
            assert Calculator.add(a, b) == result
        elif operation == 'subtract':
            result = a - b
            assert Calculator.subtract(a, b) == result
        elif operation == 'multiply':
            result = a * b
            assert Calculator.multiply(a, b) == result
        elif operation == 'divide':
            if b != 0:  # Handling division by zero
                result = a / b
                assert Calculator.divide(a, b) == result
            else:
                assert b != 0, "Division by zero is not allowed."
            

