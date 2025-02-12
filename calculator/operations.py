"""
Operations module

This module defines basic arithmetic operations such as addition, subtraction,
multiplication, and division. Each operation takes two numbers as input and 
returns the result.
"""

def add(a, b):
    """Return the sum of a and b."""
    return a + b

def subtract(a, b):
    """Return the difference between a and b."""
    return a - b

def multiply(a, b):
    """Return the product of a and b."""
    return a * b

def divide(a, b):
    """Return the quotient of a divided by b."""
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b
