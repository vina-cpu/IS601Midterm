'''My Tests for Calculator Class'''
from typing import Callable, List
from decimal import Decimal
import pytest
from faker import Faker
from calculator.operation import Operation
from calculator import Calculator

fake = Faker()
operationsList: List[Callable[[Decimal, Decimal], Decimal]] = [Operation.add, Operation.subtract, Operation.multiply, Operation.divide]

def test_calculator_new():
    '''Test for a new instance of Calculator'''
    a: Decimal = fake.random_number()
    b: Decimal = fake.random_number()
    oper: Callable[[Decimal, Decimal], Decimal] = fake.random_element(operationsList)
    assert Calculator.new(a, b, oper) == oper(a, b)

def test_calculator_add():
    '''Test for adding in Calculator instance'''
    a: Decimal = fake.random_number()
    b: Decimal = fake.random_number()
    assert Calculator.add(a, b) == Operation.add(a, b)

def test_calculator_subtract():
    '''Test for subtractingin Calculator instance'''
    a: Decimal = fake.random_number()
    b: Decimal = fake.random_number()
    assert Calculator.subtract(a, b) == Operation.subtract(a, b)

def test_calculator_multiply():
    '''Test for multiplying in Calculator instance'''
    a: Decimal = fake.random_number()
    b: Decimal = fake.random_number()
    assert Calculator.multiply(a, b) == Operation.multiply(a, b)

def test_calculator_divide():
    '''Test for dividing in Calculator instance'''
    a: Decimal = fake.random_number()
    b: Decimal = fake.random_number()
    if b != 0:
        assert Calculator.divide(a, b) == Operation.divide(a, b)

def test_calculator_divide_0():
    '''Test for dividing by 0 in Calculator instance'''
    a: Decimal = fake.random_number()
    with pytest.raises(ValueError, match = "Division by zero"):
        Calculator.divide(a, 0)
