import os
import importlib
from decimal import Decimal
from calculator.commands.command import Command

class Calculator:
    def __init__(self):
        self.commands = {}
        self._load_plugins()

    def _load_plugins(self):
        """Dynamically load all plugins from the plugins directory."""
        plugins_dir = os.path.join(os.path.dirname(__file__), "..", "plugins")
        for filename in os.listdir(plugins_dir):
            if filename.endswith(".py") and filename != "__init__.py":
                module_name = filename[:-3]  # Remove .py extension
                module = importlib.import_module(f"plugins.{module_name}")
                for attribute_name in dir(module):
                    attribute = getattr(module, attribute_name)
                    if isinstance(attribute, type) and issubclass(attribute, Command) and attribute != Command:
                        command_name = module_name  # Use the filename as the command name
                        self.commands[command_name] = attribute()
        # Add the menu command after loading all plugins
        self.commands["menu"] = MenuCommand(self.commands.keys())

    def run(self):
        """Run the interactive REPL for the calculator."""
        print("Welcome to the Interactive Calculator!")
        self.commands["menu"].execute()

        while True:
            user_input = input("Enter command: ").strip().lower()
            if user_input == "exit":
                print("Exiting calculator. Goodbye!")
                break
            if user_input in self.commands:
                if user_input == "menu":
                    self.commands[user_input].execute()
                else:
                    try:
                        a = Decimal(input("Enter first number: "))
                        b = Decimal(input("Enter second number: "))
                        result = self.commands[user_input].execute(a, b)
                        print(f"Result: {result}")
                    except ValueError as e:
                        print(f"Error: {e}")
            else:
                print("Invalid command. Type 'menu' to see available commands.")