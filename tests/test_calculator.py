'''My Calculator Test'''
from calculator import Calculator

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
    