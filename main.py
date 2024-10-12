import sys
from calculator import Calculator  # Assuming Calculator is defined elsewhere

class OperationCommand:
    def __init__(self, calculator, operation_name, a, b):
        self.calculator = calculator
        self.operation_name = operation_name
        self.a = a
        self.b = b

    def execute(self):
        # Retrieve the operation method from the Calculator class using getattr
        operation_method = getattr(self.calculator, self.operation_name, None)
        if operation_method:
            return operation_method(self.a, self.b)
        else:
            raise ValueError(f"Unknown operation: {self.operation_name}")

def calculate_and_print(a, b, operation):
    try:
        # Convert input values to float
        a = float(a)
        b = float(b)
    except ValueError:
        raise ValueError(f"Invalid number input: {a} or {b} is not a valid number.")

    # Perform the operations and calculate result
    if operation == 'add':
        result = a + b
    elif operation == 'subtract':
        result = a - b
    elif operation == 'multiply':
        result = a * b
    elif operation == 'divide':
        if b == 0:
            raise ValueError("Cannot divide by zero")
        result = a / b
    else:
        raise ValueError(f"Unknown operation: {operation}")
    
    # Remove decimal point if result is a whole number
    if result.is_integer():
        result = int(result)
        a = int(a)
        b = int(b)
    
    print(f"The result of {a} {operation} {b} is equal to {result}")

def main():
    if len(sys.argv) != 4:
        print("Usage: python calculator_main.py <number1> <number2> <operation>")
        sys.exit(1)

    _, a, b, operation_name = sys.argv

    try:
        calculate_and_print(a, b, operation_name)
    except ValueError as e:
        print(e)
        sys.exit(1)

if __name__ == '__main__':
    main()
