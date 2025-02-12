from calculator import Calculator

def test_addition():
    '''Test that addition function works'''
    assert Calculator.add(15, 25) == 40

def test_subtraction():
    '''Test that subtraction function works'''
    assert Calculator.subtract(100, 60) == 40

def test_divide():
    '''Test that division function works'''
    assert Calculator.divide(48, 8) == 6

def test_multiply():
    '''Test that multiplication function works'''
    assert Calculator.multiply(4, 9) == 36
