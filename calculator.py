# Simple calculator program

# 1. Function to perform the arithmetic operations

def calculate(number1, number2, operation):
    if operation == '+':
        return number1 + number2
    elif operation == '-':
        return number1 - number2
    elif operation == '*':
        return number1 * number2
    elif operation == '/':
        if number2 == 0:
            return "Error! Division by zero."
        return number1 / number2
    else:
        return "Invalid operation!"

# Main code
try:
    # Take input from the user
    number1 = float(input("Enter the first number: "))
    number2 = float(input("Enter the second number: "))
    operation = input("Enter the operation (+, -, *, /): ")

    # Perform the calculation and display the result
    result = calculate(number1, number2, operation)
    print(f"Result: {result}")

except ValueError:
    print("Invalid input! Please enter a valid number.")
