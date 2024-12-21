class Calculator:
    def __init__(self):
        self.result = 0

    def add(self, x, y):
        """Add two numbers"""
        self.result = x + y
        return self.result

    def subtract(self, x, y):
        """Subtract y from x"""
        self.result = x - y
        return self.result

    def multiply(self, x, y):
        """Multiply two numbers"""
        self.result = x * y
        return self.result

    def divide(self, x, y):
        """Divide x by y"""
        if y == 0:
            raise ValueError("Cannot divide by zero!")
        self.result = x / y
        return self.result

def main():
    calc = Calculator()
    
    # Test calculations
    print(f"10 + 5 = {calc.add(10, 5)}")
    print(f"10 - 5 = {calc.subtract(10, 5)}")
    print(f"10 * 5 = {calc.multiply(10, 5)}")
    print(f"10 / 5 = {calc.divide(10, 5)}")

if __name__ == "__main__":
    main()