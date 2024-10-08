from faker import Faker

faker = Faker()
'''My Calculator Test'''
from calculator import Calculator

<<<<<<< HEAD
def test_operations(generate_test_data):
    for a, b, operation in generate_test_data:
        if operation == 'add':
            result = a + b
            assert add(a, b) == result
        elif operation == 'subtract':
            result = a - b
            assert subtract(a, b) == result
            
=======
def test_addition():
    '''Test that the addition function works.'''
    assert Calculator.add(3, 5) == 8

def test_subtraction():
    '''Test that the subtraction function works.'''
    assert Calculator.subtract(10, 4) == 6

def test_divide():
    '''Test that the division function works.'''
    assert Calculator.divide(12, 4) == 3

def test_multiply():
    '''Test that the multiplication function works.'''
    assert Calculator.multiply(3, 7) == 21
    
>>>>>>> part3
