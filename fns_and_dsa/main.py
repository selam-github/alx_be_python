# main.py

from arithmetic_operations import perform_operation
 print("Arithmetic Operations")
 num1 = float(input("Enter the first number: "))
 num2 = float(input("Enter the second number: "))
 operation = input("Enter the operation (add, subtract, multiply, divide): ")
# Example usage:
num1 = 5.0
num2 = 6.0
# Addition
result_add = perform_operation(num1, num2, 'add')
    print(f"Result: {result_add}")
# Subtraction
result_subtract = perform_operation(num1, num2, 'subtract')
    print(f"result: {result_subtract}")
# Multiplication
result_multiply = perform_operation(num1, num2, 'multiply')
    print(f"result: {result_multiply}")
# Division
result_divide = perform_operation(num1, num2, 'divide')
if isinstance(result_divide, float):
        print(f"result: {result_divide}")
    else:
            print(f" error: {result_divide}")
