import os
import importlib
import logging
import logging.config
from dotenv import load_dotenv
from decimal import Decimal
from calculator.commands.add import AddCommand
from calculator.commands.subtract import SubtractCommand
from calculator.commands.multiply import MultiplyCommand
from calculator.commands.divide import DivideCommand
from calculator.commands.menu import MenuCommand
from calculator.commands.command import Command

class Calculator:
    def __init__(self):
        # Load environment variables
        load_dotenv()
        self.settings = self.load_environment_variables()

        # Configure logging
        self.configure_logging()

        # Initialize the commands dictionary with built-in commands
        self.commands = {
            "add": AddCommand(),
            "subtract": SubtractCommand(),
            "multiply": MultiplyCommand(),
            "divide": DivideCommand(),
        }

        # Load plugins dynamically
        self._load_plugins()

        # Add the menu command after the commands dictionary is fully populated
        self.commands["menu"] = MenuCommand(self.commands.keys())

        logging.info("Calculator initialized successfully.")

    def configure_logging(self):
        """Configure logging to output logs to a file."""
        os.makedirs('logs', exist_ok=True)
        logging_conf_path = 'logging.conf'
        
        if os.path.exists(logging_conf_path):
            logging.config.fileConfig(logging_conf_path, disable_existing_loggers=False)
        else:
            logging.basicConfig(filename='logs/app.log', level=logging.INFO, 
                                format='%(asctime)s - %(levelname)s - %(message)s')
        
        logging.info("Logging configured.")

    def load_environment_variables(self):
        """Load and return environment variables."""
        settings = {key: value for key, value in os.environ.items()}
        settings.setdefault('ENVIRONMENT', 'PRODUCTION')  # Default environment setting
        logging.info("Environment variables loaded.")
        return settings

    def _load_plugins(self):
        """Dynamically load plugins from the plugins directory."""
        plugins_dir = "plugins"
        if os.path.exists(plugins_dir):
            for filename in os.listdir(plugins_dir):
                if filename.endswith(".py") and filename != "__init__.py":
                    module_name = filename[:-3]  # Remove .py extension
                    try:
                        module = importlib.import_module(f"plugins.{module_name}")
                        for attr_name in dir(module):
                            attr = getattr(module, attr_name)
                            if isinstance(attr, type) and issubclass(attr, Command) and attr != Command:
                                # Skip MenuCommand as it requires special handling
                                if attr.__name__ != "MenuCommand":
                                    command_name = module_name  # Use the module name as the command name
                                    self.commands[command_name] = attr()  # Instantiate the command
                                    logging.info(f"Plugin '{command_name}' loaded successfully.")
                    except ImportError as e:
                        logging.error(f"Error loading plugin {module_name}: {e}")

    def run(self):
        """Run the interactive REPL for the calculator."""
        print("Welcome to the Interactive Calculator!")
        logging.info("Calculator application started.")

        # Display the menu at the start
        self.commands["menu"].execute()

        while True:
            user_input = input("Enter command: ").strip().lower()
            if user_input == "exit":
                print("Exiting calculator. Goodbye!")
                logging.info("Calculator application exited.")
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
                        logging.info(f"Command '{user_input}' executed successfully with inputs {a}, {b}. Result: {result}")
                    except ValueError as e:
                        print(f"Error: {e}")
                        logging.error(f"Invalid input error: {e}")
            else:
                print("Invalid command. Type 'menu' to see available commands.")
                logging.warning(f"Invalid command entered: {user_input}")
