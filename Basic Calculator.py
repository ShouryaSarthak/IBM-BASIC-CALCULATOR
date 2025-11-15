class Calculator:
    """A basic calculator class with arithmetic operations"""
    
    def add(self, a, b):
        """Add two numbers"""
        return a + b
    
    def subtract(self, a, b):
        """Subtract b from a"""
        return a - b
    
    def multiply(self, a, b):
        """Multiply two numbers"""
        return a * b
    
    def divide(self, a, b):
        """Divide a by b with error handling"""
        if b == 0:
            raise ValueError("Error: Division by zero is not allowed")
        return a / b



def main():
    """Main function to run the calculator"""
    calc = Calculator()
    
    print("=== Basic Calculator ===")
    print ("no. 1 addition")
    print("no. 2 subtraction")
    print("no. 3 multiplication")
    print("no.4 division")
    print("Operations: +, -, *, /")
    print("Type 'quit' to exit\n")
    
    while True:
        try:
            # Get user input
            user_input = input("Enter operation (or 'quit'): ").strip().lower()
            
            if user_input == 'quit':
                print("Thank you for using the calculator!")
                break
            
            # Get numbers
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            
            # Conditional to select operation
            if user_input == '+':
                result = calc.add(num1, num2)
                print(f"Result: {num1} + {num2} = {result}\n")
            elif user_input == '-':
                result = calc.subtract(num1, num2)
                print(f"Result: {num1} - {num2} = {result}\n")
            elif user_input == '*':
                result = calc.multiply(num1, num2)
                print(f"Result: {num1} * {num2} = {result}\n")
            elif user_input == '/':
                result = calc.divide(num1, num2)
                print(f"Result: {num1} / {num2} = {result}\n")
            else:
                print("Error: Invalid operation. Please use +, -, *, or /\n")
        
        except ValueError as e:
            print(f"{e}\n")
        except Exception as e:
            print(f"Error: {e}\n")


if __name__ == "__main__":
    main()
