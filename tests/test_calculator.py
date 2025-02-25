from decimal import Decimal

import pytest
from calculator import Calculator
from calculator.commands.add import AddCommand
from calculator.commands.subtract import SubtractCommand
from calculator.commands.multiply import MultiplyCommand
from calculator.commands.divide import DivideCommand

def test_calculator_add():
    '''Test that addition command works'''
    calc = Calculator()
    result = calc.commands["add"].execute(Decimal('15'), Decimal('25'))
    assert result == Decimal('40'), "Add command failed in Calculator"

def test_calculator_subtract():
    '''Test that subtraction command works'''
    calc = Calculator()
    result = calc.commands["subtract"].execute(Decimal('100'), Decimal('60'))
    assert result == Decimal('40'), "Subtract command failed in Calculator"

def test_calculator_multiply():
    '''Test that multiplication command works'''
    calc = Calculator()
    result = calc.commands["multiply"].execute(Decimal('4'), Decimal('9'))
    assert result == Decimal('36'), "Multiply command failed in Calculator"

def test_calculator_divide():
    '''Test that division command works'''
    calc = Calculator()
    result = calc.commands["divide"].execute(Decimal('48'), Decimal('8'))
    assert result == Decimal('6'), "Divide command failed in Calculator"

def test_calculator_divide_by_zero():
    '''Test that division by zero raises an error'''
    calc = Calculator()
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        calc.commands["divide"].execute(Decimal('10'), Decimal('0'))
