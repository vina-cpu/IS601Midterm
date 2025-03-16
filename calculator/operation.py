from decimal import Decimal

class Operation:
    @staticmethod
    def add(a: Decimal,b: Decimal) -> Decimal:
        return a + b

    @staticmethod
    def subtract(a: Decimal,b: Decimal) -> Decimal:
        return a - b

    @staticmethod
    def multiply(a: Decimal,b: Decimal) -> Decimal:
        return a * b

    @staticmethod
    def divide(a: Decimal,b: Decimal) -> Decimal:
        if b == 0: # here i used LBYL because I am declaring an error here, not handling an active error, so it would go through the try case first and print out a different error than what i want
            raise ValueError("Division by zero")
        return a / b;