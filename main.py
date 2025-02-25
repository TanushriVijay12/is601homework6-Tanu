import sys
from decimal import Decimal, InvalidOperation
from calculator.commands.add import AddCommand
from calculator.commands.subtract import SubtractCommand
from calculator.commands.multiply import MultiplyCommand
from calculator.commands.divide import DivideCommand

class Calculator:
    def __init__(self):
        self.commands = {
            "add": AddCommand(),
            "subtract": SubtractCommand(),
            "multiply": MultiplyCommand(),
            "divide": DivideCommand(),
        }

    def run(self):
        print("Welcome to the Interactive Calculator!")
        print("Available commands: add, subtract, multiply, divide")
        print("Type 'exit' to quit.")

        while True:
            user_input = input("Enter command: ").strip().lower()
            if user_input == "exit":
                print("Exiting calculator. Goodbye!")
                break
            if user_input in self.commands:
                try:
                    a = Decimal(input("Enter first number: "))
                    b = Decimal(input("Enter second number: "))
                    result = self.commands[user_input].execute(a, b)
                    print(f"Result: {result}")
                except InvalidOperation:
                    print("Invalid number input. Please enter valid numbers.")
                except ZeroDivisionError:
                    print("Cannot divide by zero.")
                except ValueError as e:
                    print(f"Error: {e}")
            else:
                print("Invalid command. Available commands: add, subtract, multiply, divide")

def calculate_and_print(a, b, operation_name):
    try:
        a_decimal, b_decimal = map(Decimal, [a, b])
        calculator = Calculator()
        if operation_name in calculator.commands:
            result = calculator.commands[operation_name].execute(a_decimal, b_decimal)
            print(f"The result of {a} {operation_name} {b} is equal to {result}")
        else:
            raise ValueError(f"Unknown operation: {operation_name}")
    except InvalidOperation:
        print(f"Invalid number input: {a} or {b} is not a valid number.")
    except ZeroDivisionError:
        print("Cannot divide by zero.")
    except ValueError as e:
        print(e)
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    if len(sys.argv) == 4:
        # Command-line mode
        _, a, b, operation_name = sys.argv
        calculate_and_print(a, b, operation_name)
    else:
        # Interactive REPL mode
        calculator = Calculator()
        calculator.run()

if __name__ == '__main__':
    main()
