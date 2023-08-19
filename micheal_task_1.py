# from art import logo
import os

def clear():
    """
    Clears the console screen.
    """
    os.system('cls' if os.name == 'nt' else 'clear')


def add(n1, n2):
    return n1 + n2


def sub(n1, n2):
    return n1 - n2


def divide(n1, n2):
    return n1 / n2


def multiply(n1, n2):
    return n1 * n2


def calculator():
    # print(logo)
    print("Simple Calculator.")
    try:
        num1 = float(input("Enter the first number: "))
    except ValueError:
        print("first number is not an integer")
        calculator()

    should_continue = True
    while should_continue:
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        operation = input("Choose an operation: ")

        try:
            num2 = float(input("Enter the second number: "))
        except ValueError:
            print("second number is not an integer")
            calculator()

        answer = ""
        operation_symbol = ""
        if operation == "1":
            operation_symbol = "+"
            answer = add(n1=num1, n2=num2)
        elif operation == "2":
            operation_symbol = "-"
            answer = sub(n1=num1, n2=num2)
        elif operation == "3":
            operation_symbol = "*"
            answer = multiply(n1=num1, n2=num2)
        elif operation == "4":
            operation_symbol = "/"
            answer = divide(n1=num1, n2=num2)
        else:
            print("Invalid option")

        print(f"Result: {num1} {operation_symbol} {num2} = {answer}")

        if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation.: ") == "y":
            num1 = answer
        else:
            should_continue = False
            clear()
            calculator()


calculator()