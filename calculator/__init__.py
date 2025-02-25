from decimal import Decimal
from calculator.commands.add import AddCommand
from calculator.commands.subtract import SubtractCommand
from calculator.commands.multiply import MultiplyCommand
from calculator.commands.divide import DivideCommand
from calculator.commands.menu import MenuCommand

class Calculator:
    def __init__(self):
        # Initialize the commands dictionary
        self.commands = {
            "add": AddCommand(),
            "subtract": SubtractCommand(),
            "multiply": MultiplyCommand(),
            "divide": DivideCommand(),
        }
        # Add the menu command
        self.commands["menu"] = MenuCommand(self.commands.keys())

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