from typing import Callable
from decimal import Decimal
from calculator.operation import Operation

class Calculation:
    def __init__(self, a: Decimal, b: Decimal, operation: Callable[[Decimal, Decimal], Decimal]):
        self.a = a
        self.b = b
        self.operation = operation
        
    def do(self) -> Decimal:
        return self.operation(self.a, self.b)
    
    @staticmethod
    def new(a: Decimal, b: Decimal, oper: Callable[[Decimal, Decimal], Decimal]):
        return Calculation(a, b, oper)

    def get_a(self) -> Decimal:
        return self.a
    
    def get_b(self) -> Decimal:
        return self.b
    
    def get_operation(self) -> Decimal:
        return self.operation