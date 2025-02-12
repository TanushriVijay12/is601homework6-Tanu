"""
This module defines the Calculator class with static methods for basic arithmetic operations 
such as addition, subtraction, multiplication, and division.
It utilizes the Calculation class to process each operation.
"""
from calculator.calculation import Calculation
from calculator.operations import add, subtract, multiply, divide

class Calculator:
    """
    A class to represent a basic calculator that performs arithmetic operations.
    
    Methods:
        add(a, b): Adds two numbers and returns the result.
        subtract(a, b): Subtracts the second number from the first and returns the result.
        multiply(a, b): Multiplies two numbers and returns the result.
        divide(a, b): Divides the first number by the second and returns the result.
    """
    @staticmethod
    def add(a,b):
        """
    Adds two numbers and returns the result.
    
    Parameters:
        a (float): The first number.
        b (float): The second number.
    
    Returns:
        float: The result of the addition.
    """
        calculation = Calculation(a, b, add)  # Pass the add function from calculator.operations
        return calculation.get_result()
    @staticmethod
    def subtract(a,b):
        """
    Subtracts the second number from the first and returns the result.
    
    Parameters:
        a (float): The first number.
        b (float): The second number.
    
    Returns:
        float: The result of the subtraction.
    """
        calculation = Calculation(a, b, subtract)  # Pass the add function
        return calculation.get_result()
    @staticmethod
    def multiply (a,b):
        """
    Multiplies two numbers and returns the result.
    
    Parameters:
        a (float): The first number.
        b (float): The second number.
    
    Returns:
        float: The result of the multiplication.
    """
        calculation = Calculation(a, b, multiply)  # Pass the add function
        return calculation.get_result()
    @staticmethod
    def divide(a,b):
        """
    Divides the first number by the second and returns the result.
    
    Parameters:
        a (float): The first number.
        b (float): The second number.
    
    Returns:
        float: The result of the division.
    
    Raises:
        ZeroDivisionError: If the second number (b) is zero.
    """
        calculation = Calculation(a, b, add)  # Pass the add function
# Or split complex expressions over multiple lines

        return calculation.get_result()
