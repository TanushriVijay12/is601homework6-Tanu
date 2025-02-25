import os
import importlib
from decimal import Decimal
from calculator.commands.add import AddCommand
from calculator.commands.subtract import SubtractCommand
from calculator.commands.multiply import MultiplyCommand
from calculator.commands.divide import DivideCommand
from calculator.commands.menu import MenuCommand

class Calculator:
    def __init__(self):
        # Initialize the commands dictionary with built-in commands
        self.commands = {
            "add": AddCommand(),
            "subtract": SubtractCommand(),
            "multiply": MultiplyCommand(),
            "divide": DivideCommand(),
        }
        # Load plugins
        self._load_plugins()
        # Add the menu command after the commands dictionary is fully populated
        self.commands["menu"] = MenuCommand(self.commands.keys())

    def _load_plugins(self):
        """Dynamically load plugins from the plugins directory."""
        plugins_dir = "plugins"
        if os.path.exists(plugins_dir):
            for filename in os.listdir(plugins_dir):
                if filename.endswith(".py") and filename != "__init__.py":
                    module_name = filename[:-3]  # Remove .py extension
                    module = importlib.import_module(f"{plugins_dir}.{module_name}")
                    for attr_name in dir(module):
                        attr = getattr(module, attr_name)
                        if isinstance(attr, type) and issubclass(attr, Command) and attr != Command:
                            command_name = module_name  # Use the module name as the command name
                            self.commands[command_name] = attr()  # Instantiate the command

    def run(self):
        """Run the interactive REPL for the calculator."""
        print("Welcome to the Interactive Calculator!")
        # Display the menu at the start
        self.commands["menu"].execute()

        while True:
            user_input = input("Enter command: ").strip().lower()
            if user_input == "exit":
                print("Exiting calculator. Goodbye!")
                break
            if user_input in self.commands:
                if user_input == "menu":
                    # Display the menu when the user types "menu"
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