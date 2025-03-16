from typing import Callable
from decimal import Decimal
from calculator.operation import Operation
from calculator.calculation import Calculation

class Calculator:
    
    @staticmethod
    def new(a: Decimal, b: Decimal, oper: Callable[[Decimal, Decimal], Decimal]) -> Decimal:
        newCalc = Calculation.new(a, b, oper)
        #History.append_calc(newCalc)
        return newCalc.do()
    
    @staticmethod
    def add(a: Decimal, b: Decimal):
        return Calculator.new(a, b, Operation.add)

    @staticmethod
    def subtract(a: Decimal, b: Decimal) -> Decimal:
        return Calculator.new(a, b, Operation.subtract)
   
    @staticmethod
    def multiply(a: Decimal, b: Decimal) -> Decimal:
        return Calculator.new(a, b, Operation.multiply)
   
    @staticmethod
    def divide(a: Decimal, b: Decimal) -> Decimal:
        return Calculator.new(a, b, Operation.divide)