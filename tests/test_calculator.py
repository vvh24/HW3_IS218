from faker import Faker

faker = Faker()
'''My Calculator Test'''
from calculator import add, subtract

def test_operations(generate_test_data):
    for a, b, operation in generate_test_data:
        if operation == 'add':
            result = a + b
            assert add(a, b) == result
        elif operation == 'subtract':
            result = a - b
            assert subtract(a, b) == result
            
