# arithmetic_operations.py

def perform_operation(num1, num2, operation):
    """" Performs basic arithmetic operations on two numbers.
        """
        if operation == 'add':
            return num1 + num2
        elif operation == 'subtract':
            return num1 - num2
        elif operation == 'multiply':
            return num1 * num2
        elif operation == 'divide': # in this case having two condition division by num1/0 and num1/num2
            if num2 == 0:
                return "Error: Division by zero!"
            else:
                 return num1 / num2
         else:
             return "Error: Invalid operation! Please use 'add', 'subtract', 'multiply', or 'divide'."
