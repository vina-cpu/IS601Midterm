'''My Tests for the Calculation Class'''
from typing import Callable, List
from decimal import Decimal
import pytest
from faker import Faker
from calculator.operation import Operation
from calculator.calculation import Calculation

fake = Faker()
operationsList: List[Callable[[Decimal, Decimal], Decimal]] = [Operation.add, Operation.subtract, Operation.multiply, Operation.divide]

def test_calculation_add():
    '''Test addition inside Calculation instance'''
    assert Calculation(3, -5, Operation.add).do() == -2
    a: Decimal = fake.random_number()
    b: Decimal = fake.random_number()
    assert Calculation(a, b, Operation.add).do() == a + b

def test_calculation_subtract():
    '''Test subtraction inside Calculation instance'''
    assert Calculation(2, -2, Operation.subtract).do() == 4
    a: Decimal = fake.random_number()
    b: Decimal = fake.random_number()
    assert Calculation(a, b, Operation.subtract).do() == a - b

def test_calculation_multiply():
    '''Test multiplication inside Calculation instance'''
    assert Calculation(3, 2, Operation.multiply).do() == 6
    a: Decimal = fake.random_number()
    b: Decimal = fake.random_number()
    assert Calculation(a, b, Operation.multiply).do() == a * b

def test_calculation_divide():
    '''Test division inside Calculation instance'''
    assert Calculation(3, 2, Operation.divide).do() == 1.5
    a: Decimal = fake.random_number()
    b: Decimal = fake.random_number()
    if b != 0:
        assert Calculation(a, b, Operation.divide).do() == a / b

def test_calculation_divide_0():
    '''Test division by zero inside Calculation instance'''
    a: Decimal = fake.random_number()
    with pytest.raises(ValueError, match = "Division by zero"):
        Calculation(a, 0, Operation.divide).do()

def test_calculation_new_calculation():
    '''Test new calculation function inside Calculation instance'''
    a: Decimal = fake.random_number()
    b: Decimal = fake.random_number()
    oper: Callable[[Decimal, Decimal], Decimal] = fake.random_element(operationsList)
    calc = Calculation.new(a, b, oper)
    assert calc.get_a() == a
    assert calc.get_b() == b
    assert calc.get_operation() == oper

def test_calculation_get_a():
    '''Test for getting a from a Calculation instance'''
    assert Calculation(2, 5, Operation.add).get_a() == 2
    a = fake.random_number()
    assert Calculation(a, 1, Operation.add).get_a() == a

def test_calculation_get_b():
    '''Test for getting b from a Calculation instance'''
    assert Calculation(1, -4, Operation.multiply).get_b() == -4
    b = fake.random_number()
    assert Calculation(1, b, Operation.subtract).get_b() == b

def test_calculation_getoperation():
    '''Test for getting an operation from a Calculation instance'''
    oper: Callable[[Decimal, Decimal], Decimal] = fake.random_element(operationsList)
    assert Calculation(1, 1, oper).get_operation().__name__ == oper.__name__
