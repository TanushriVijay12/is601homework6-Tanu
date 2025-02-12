from decimal import Decimal
import pytest
from calculator.calculation import Calculation
from calculator.operations import add, subtract, multiply, divide

def test_operation_add():
    '''Testing the addition operation'''
    calculation = Calculation(Decimal('15'), Decimal('7'), add)
    assert calculation.perform() == Decimal('22'), "Add operation failed"

def test_operation_subtract():
    '''Testing the subtract operation'''
    calculation = Calculation(Decimal('25'), Decimal('8'), subtract)
    assert calculation.perform() == Decimal('17'), "Subtract operation failed"

def test_operation_multiply():
    '''Testing the multiply operation'''
    calculation = Calculation(Decimal('12'), Decimal('6'), multiply)
    assert calculation.perform() == Decimal('72'), "Multiply operation failed"

def test_operation_divide():
    '''Testing the divide operation'''
    calculation = Calculation(Decimal('40'), Decimal('8'), divide)
    assert calculation.perform() == Decimal('5'), "Divide operation failed"

def test_divide_by_zero():
    '''Testing the divide by zero exception'''
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        calculation = Calculation(Decimal('20'), Decimal('0'), divide)
        calculation.perform()
