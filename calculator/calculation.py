"""
Calculation module

This module contains the Calculation class, which is responsible for storing
two numbers and an operation function. It applies the operation to the numbers 
and returns the result. The class is designed to separate the logic of the 
calculation from the operation itself.
"""
class Calculation:
    """
    A class to perform a calculation using a given operation.

    This class stores two numbers, `a` and `b`, and an operation function. It
    then applies the operation to the numbers and returns the result.

    Attributes:
        a (float): The first number in the operation.
        b (float): The second number in the operation.
        operation (function): The function that defines the operation to be performed.
    """

    def __init__(self, a, b, operation):
        """
        Initializes the Calculation instance with two numbers and an operation.

        Parameters:
            a (float): The first number in the operation.
            b (float): The second number in the operation.
            operation (function): The operation function (e.g., add, subtract, multiply, divide).
        """
        self.a = a
        self.b = b
        self.operation = operation

    def get_result(self):
        """
        Applies the stored operation on the two numbers and returns the result.

        Returns:
            float: The result of applying the operation to the two numbers.
        """
        return self.operation(self.a, self.b)
