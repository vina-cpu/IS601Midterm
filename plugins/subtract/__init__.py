from decimal import Decimal, InvalidOperation
from calculator import Calculator
from commands.command import Command

class SubtractCommand(Command):
    description = "Type 'subtract' to subtract one number from another"
    def execute(self):
        print("What is your first number:")
        num1str: str = input(">>> ").strip()
        print("What is your second number:")
        num2str: str = input(">>> ").strip()
        print("Calculating ... ")
        try:
            num1, num2 = map(Decimal, [num1str, num2str])
            result = Calculator.subtract(num1, num2)
            print(f"The result of {num1} subtract {num2} is equal to {result}")
        except InvalidOperation:
            print(f"Invalid number input: {num1str} or {num2str} is not a valid number.")      
        except Exception as e: #line missed in cov - don't know how to test this
            print(f"An error occured: {e}") #line missed in cov - don't know how to test this 

command = SubtractCommand()