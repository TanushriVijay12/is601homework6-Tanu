'''Test Calculator Operations

This module contains test cases for the basic calculator operations:
addition, subtraction, multiplication, and division. Each test
checks that the respective function works correctly.
'''

from calculator.operations import add, multiply, subtract, divide

def test_addition():
    '''Test that addition function works '''    
    assert add(2, 2) == 4

def test_subtraction():
    '''Test that subtraction function works '''    
    assert subtract(2, 2) == 0

def test_multiplication():
    '''Test that multiplication function works'''
    assert multiply(2, 2) == 4

def test_division():
    '''Test that division function works'''
    assert divide(2, 2) == 1
