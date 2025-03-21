'''My Tests for the Operation Class'''
from decimal import Decimal
import pytest
from faker import Faker
from calculator.operation import Operation

fake = Faker()

def test_add():
    '''Test addition function'''
    assert Operation.add(2, -3) == -1
    a: Decimal = fake.random_number()
    b: Decimal = fake.random_number()
    assert Operation.add(a, b) == a + b

def test_subtract():
    '''Test subtraction function'''
    assert Operation.subtract(3, 3) == 0
    a: Decimal = fake.random_number()
    b: Decimal = fake.random_number()
    assert Operation.subtract(a, b) == a - b

def test_multiply():
    '''Test multiplication function'''
    assert Operation.multiply(2, 4) == 8
    a: Decimal = fake.random_number()
    b: Decimal = fake.random_number()
    assert Operation.multiply(a, b) == a * b

def test_divide():
    '''Test divide function'''
    assert Operation.divide(12, 4) == 3
    a: Decimal = fake.random_number()
    b: Decimal = fake.random_number()
    if b != 0:
        assert Operation.divide(a, b) == a / b

def test_divide_by_zero():
    '''Test divide function with 0'''
    a: Decimal = fake.random_number()
    with pytest.raises(ValueError, match = "Division by zero"):
        Operation.divide(a, 0)
