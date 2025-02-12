from decimal import Decimal
import pytest
from calculator.calculation import Calculation
from calculator.operations import add, subtract, multiply, divide

# Parametrized test for operations.
@pytest.mark.parametrize("a, b, operation, expected", [
    (Decimal('15'), Decimal('5'), add, Decimal('20')),  # Test addition
    (Decimal('25'), Decimal('8'), subtract, Decimal('17')),  # Test subtraction
    (Decimal('12'), Decimal('6'), multiply, Decimal('72')),  # Test multiplication
    (Decimal('40'), Decimal('8'), divide, Decimal('5')),  # Test division
    (Decimal('10.75'), Decimal('2.75'), add, Decimal('13.5')),  # Test addition with decimals
    (Decimal('15.5'), Decimal('5.5'), subtract, Decimal('10')),  # Test subtraction with decimals
    (Decimal('7.5'), Decimal('3'), multiply, Decimal('22.5')),  # Test multiplication with decimals
    (Decimal('20'), Decimal('4'), divide, Decimal('5')),  # Test division with decimals
])
def test_calculation_operations(a, b, operation, expected):
    calc = Calculation(a, b, operation)
    assert calc.perform() == expected, f"Failed {operation.__name__} operation with {a} and {b}"

def test_calculation_repr():
    calc = Calculation(Decimal('15'), Decimal('7'), add)
    expected_repr = "Calculation(15, 7, add)"
    assert calc.__repr__() == expected_repr, "The __repr__ method output does not match the expected string."

def test_divide_by_zero():
    calc = Calculation(Decimal('20'), Decimal('0'), divide)
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        calc.perform()
