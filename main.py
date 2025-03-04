import logging
import os
from decimal import Decimal, InvalidOperation
from dotenv import load_dotenv  # Load environment variables
from calculator import Calculator

# Load environment variables from .env file
load_dotenv()

# Get environment variables
LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO").upper()  # Default to INFO if not set
DEBUG_MODE = os.getenv("DEBUG_MODE", "False").lower() == "true"  # Default to False, convert string to boolean
LOG_FILE = os.getenv("LOG_FILE", "app.log")  # Default log file name

# Configure logging based on environment variables
logging.basicConfig(
    filename=LOG_FILE,
    level=getattr(logging, LOG_LEVEL, logging.INFO),  # Convert string to logging level (e.g., INFO -> logging.INFO)
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# If DEBUG_MODE is True, also output logs to the console
if DEBUG_MODE:
    console_handler = logging.StreamHandler()
    console_handler.setLevel(getattr(logging, LOG_LEVEL, logging.INFO))
    console_handler.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(message)s"))
    logging.getLogger().addHandler(console_handler)

def calculate_and_print(a, b, operation_name):
    try:
        a_decimal, b_decimal = map(Decimal, [a, b])
        calculator = Calculator()
        if operation_name in calculator.commands:
            result = calculator.commands[operation_name].execute(a_decimal, b_decimal)
            message = f"The result of {a} {operation_name} {b} is equal to {result}"
            logging.info(message)  # Log success
            if DEBUG_MODE:
                print(message)  # Print only if DEBUG_MODE is enabled
        else:
            raise ValueError(f"Unknown operation: {operation_name}")
    except InvalidOperation:
        error_message = f"Invalid number input: {a} or {b} is not a valid number."
        logging.error(error_message)  # Log error
        if DEBUG_MODE:
            print(error_message)
    except ValueError as e:
        logging.error(str(e))  # Log error
        if DEBUG_MODE:
            print(e)

def main():
    import sys
    if len(sys.argv) == 4:
        _, a, b, operation_name = sys.argv
        calculate_and_print(a, b, operation_name)
    else:
        calculator = Calculator()
        calculator.run()

if __name__ == '__main__':
    main()
