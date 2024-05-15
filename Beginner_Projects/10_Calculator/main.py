# Calculator different functions like add, subtract, divide and multiply

# Add function:
def add(n1, n2):
    return n1 + n2

# Subtract function: 
def subtract(n1, n2):
    return n1 - n2

# Multiply function:
def multiply(n1, n2):
    return n1 * n2

# Divide function: 
def divide(n1, n2):
    return n1 / n2

#Dictionary, key is the symbol and value is the name of the function
operations = {
    "+" : add,
    "-" : subtract,
    "*" : multiply,
    "/" : divide,
 }

# Import logo of calculator
from art import logo

def calculator():
    print(logo)    
    num1 = float(input("What's the first number?: "))
    for symbol in operations: 
        print(symbol)
    should_continue = True

    while should_continue:
        operation_symbol = input("Pick an operation: ")
        num2 = float(input("What is the next number?: "))
        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1, num2)

        print(f"{num1} {operation_symbol} {num2} = {answer}")
        if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ") == "y": 
            num1 = answer
        else: 
            should_continue = False
            calculator()
 
calculator()
