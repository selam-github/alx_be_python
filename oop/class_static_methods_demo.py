#class_static_methods_demo.py
class Calculator:
    # Class Attribute
    calculation_type = "Arithmetic Operations"

    # Static Method
    @staticmethod
    def add(a, b):
        return a + b

    # Class Method
    @classmethod
    def multiply(cls, a, b):
        print(f"Calculation type: {cls.calculation_type}")
        return a * b

def main():
    # Using the static method
    sum_result = Calculator.add(5, 7)
    print(f"The sum of 5 and 7 is: {sum_result}")

    # Using the class method
    product_result = Calculator.multiply(4, 6)
    print(f"The product of 4 and 6 is: {product_result}")

if __name__ == "__main__":
    main()
