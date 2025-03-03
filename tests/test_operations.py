from decimal import Decimal
import pytest
from calculator.commands.add import AddCommand
from calculator.commands.subtract import SubtractCommand
from calculator.commands.multiply import MultiplyCommand
from calculator.commands.divide import DivideCommand

def test_add_command():
    '''Testing the addition command'''
    cmd = AddCommand()
    assert cmd.execute(Decimal('15'), Decimal('7')) == Decimal('22'), "Add command failed"

def test_subtract_command():
    '''Testing the subtraction command'''
    cmd = SubtractCommand()
    assert cmd.execute(Decimal('25'), Decimal('8')) == Decimal('17'), "Subtract command failed"

def test_multiply_command():
    '''Testing the multiplication command'''
    cmd = MultiplyCommand()
    assert cmd.execute(Decimal('12'), Decimal('6')) == Decimal('72'), "Multiply command failed"

def test_divide_command():
    '''Testing the division command'''
    cmd = DivideCommand()
    assert cmd.execute(Decimal('40'), Decimal('8')) == Decimal('5'), "Divide command failed"

def test_divide_by_zero_command():
    '''Testing the divide by zero exception in the command'''
    cmd = DivideCommand()
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        cmd.execute(Decimal('20'), Decimal('0'))
