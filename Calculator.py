# Arithmetic functions
def add(num1, num2):
    """Returns the sum of two numbers"""
    return num1 + num2

def subtract(num1, num2):
    """Returns the difference between two numbers"""
    return num1 - num2

def multiply(num1, num2):
    """Returns the product of two numbers"""
    return num1 * num2

def divide(num1, num2):
    """Returns the quotient of two numbers"""
    return num1 / num2
def power(num1, num2):
    """Returns num1 raised to the power of num2"""
    return num1 ** num2

########
def calculator():
    print("Welcome to Simple Calculator!")
    print("Operations available: +, -, *, /, ^ (power)")
    
    while True:
        try:
            num1 = float(input("Enter first number: "))
            operation = input("Enter operation (+, -, *, /, ^): ")
            num2 = float(input("Enter second number: "))
            
            # Update operation check to include '^'
            if operation not in ['+', '-', '*', '/', '^']:
                print("Error: Invalid operation. Please use +, -, *, /, or ^")
                continue
                
            # Add power operation to calculation logic
            if operation == '+':
                result = add(num1, num2)
            elif operation == '-':
                result = subtract(num1, num2)
            elif operation == '*':
                result = multiply(num1, num2)
            elif operation == '/':
                try:
                    result = divide(num1, num2)
                except ZeroDivisionError:
                    print("Error: Cannot divide by zero!")
                    continue
            elif operation == '^':
                result = power(num1, num2)
                
            print(f"Result: {num1} {operation} {num2} = {result}")
            
        except ValueError:
            print("Error: Please enter valid numbers!")
            continue
            
        another_calculation = input("Do another calculation? (yes/no): ").lower()
        if another_calculation != 'yes':
            print("Goodbye!")
            break
calculator()
