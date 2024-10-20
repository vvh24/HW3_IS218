import sys
import logging
from calculator import Calculator  # Assuming Calculator is defined elsewhere

# Configure logging to log to 'logs/app.log'
logging.basicConfig(
    filename='logs/app.log',    # Logs will be written to 'logs/app.log'
    level=logging.DEBUG,        # Set the logging level (DEBUG logs everything)
    format='%(asctime)s - %(levelname)s - %(message)s'
)

class OperationCommand:
    def __init__(self, calculator, operation_name, a, b):
        self.calculator = calculator
        self.operation_name = operation_name
        self.a = a
        self.b = b

    def execute(self):
        operation_method = getattr(self.calculator, self.operation_name, None)
        if operation_method:
            logging.debug(f"Executing {self.operation_name} with values {self.a} and {self.b}")
            return operation_method(self.a, self.b)
        else:
            logging.error(f"Unknown operation: {self.operation_name}")
            raise ValueError(f"Unknown operation: {self.operation_name}")

def calculate_and_print(a, b, operation):
    try:
        a = float(a)
        b = float(b)
        logging.debug(f"Converted inputs to floats: {a}, {b}")
    except ValueError:
        logging.error(f"Invalid number input: {a} or {b} is not a valid number.")
        raise ValueError(f"Invalid number input: {a} or {b} is not a valid number.")

    try:
        if operation == 'add':
            result = a + b
        elif operation == 'subtract':
            result = a - b
        elif operation == 'multiply':
            result = a * b
        elif operation == 'divide':
            if b == 0:
                logging.error("Attempted to divide by zero")
                raise ValueError("Cannot divide by zero")
            result = a / b
        else:
            logging.error(f"Unknown operation: {operation}")
            raise ValueError(f"Unknown operation: {operation}")
        
        if result.is_integer():
            result = int(result)
            a = int(a)
            b = int(b)
        
        logging.info(f"The result of {a} {operation} {b} is equal to {result}")
        print(f"The result of {a} {operation} {b} is equal to {result}")
    
    except ValueError as e:
        logging.error(f"Error in calculation: {e}")
        raise

def main():
    if len(sys.argv) != 4:
        logging.error("Invalid number of arguments")
        print("Usage: python calculator_main.py <number1> <number2> <operation>")
        sys.exit(1)

    _, a, b, operation_name = sys.argv

    try:
        calculate_and_print(a, b, operation_name)
    except ValueError as e:
        logging.error(f"Exiting due to error: {e}")
        print(e)
        sys.exit(1)

if __name__ == '__main__':
    main()