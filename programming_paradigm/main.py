import sys

def divide(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."
    except ValueError:
        return "Error: Invalid input. Please provide numbers."
    return result

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python robust_division_calculator.py <numerator> <denominator>")
        sys.exit(1)
    
    try:
        numerator = float(sys.argv[1])
        denominator = float(sys.argv[2])
    except ValueError:
        print("Error: Invalid input. Please provide numbers.")
        sys.exit(1)
    
    result = divide(numerator, denominator)
    print(result)

