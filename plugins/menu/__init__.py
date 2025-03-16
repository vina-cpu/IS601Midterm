import logging
import importlib
import pkgutil
import plugins
from decimal import Decimal, InvalidOperation
from history import History
from commands.command import Command

class MenuCommand(Command):
    description = "Type 'menu' to look at the menu of commands"
    
    def execute(self):
        print(f"MENU")
        try:
            for _, name, _ in pkgutil.iter_modules(plugins.__path__):
                module = importlib.import_module(f"plugins.{name}.__init__")
                if hasattr(module, "command"):
                    print(module.command.description)
            
        except Exception as e:
            print(f"An error occured: {e}")

command = MenuCommand()