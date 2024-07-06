# main.py

from arithmetic_operations import perform_operation
# Example usage:
num1 = 5.0
num2 = 6.0
# Addition
result_add = perform_operation(num1, num2, 'add')
    print(f"Addition result: {result_add}")
# Subtraction
result_subtract = perform_operation(num1, num2, 'subtract')
    print(f"Subtraction result: {result_subtract}")
# Multiplication
result_multiply = perform_operation(num1, num2, 'multiply')
    print(f"Multiplication result: {result_multiply}")
# Division
result_divide = perform_operation(num1, num2, 'divide')
if isinstance(result_divide, float):
        print(f"Division result: {result_divide}")
    else:
            print(f"Division error: {result_divide}")
