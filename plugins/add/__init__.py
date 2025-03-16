import logging
from decimal import Decimal, InvalidOperation
from calculator import Calculator
from commands.command import Command

class AddCommand(Command):
    description = "Type 'add' to add two numbers"
    
    def execute(self):
        print("What is your first number:")
        num1str: str = input(">>> ").strip()
        print("What is your second number:")
        num2str: str = input(">>> ").strip()
        print("Calculating ... ")
        try:
            num1, num2 = map(Decimal, [num1str, num2str])
            result = Calculator.add(num1, num2)
            logging.info(f"The result of {num1} add {num2} is equal to {result}")
            print(f"The result of {num1} add {num2} is equal to {result}")
        except InvalidOperation:
            print(f"Invalid number input: {num1str} or {num2str} is not a valid number.") 
            logging.error(f"Invalid number input: {num1str} or {num2str} is not a valid number.")
        except Exception as e: #line missed in cov - don't know how to test this
            print(f"An error occured: {e}") #line missed in cov - don't know how to test this
            logging.error(f"While attempting to add, an error occured: {e}")

command = AddCommand()