"""
    Author: Olaoluwa Idowu
    Date: 15-08-23
    Title: PME task1 - calculator
"""


def execute(operation,x,y):

    try:
        if operation == 1:
            return x + y
        elif operation == 2:
            return x - y
        elif operation == 3:
            return x * y
        else:
            return x / y
    except ZeroDivisionError as e:
        return e


    # if operation == 1:
    #     return x + y
    # elif operation == 2:
    #     return x - y
    # elif operation == 3:
    #     return x * y
    # elif y == 0:     # handles division by zero gracefully
    #     return "Undefine: Division by zero"
    # else:
    #     return x / y


def get_number(position, max_trials=5):     # function to request for user's input
    
    # loops to track number of trials
    for trials in range(max_trials):
        try:
            number = float(input(f"Enter the {position}: "))
            return number
        
        except ValueError:
            # end program if max trials exceeded
            if trials == 4:
                print("Invalid input. Please enter a valid number.")
                print(f"{max_trials} Trials Exceeded! Program Ended.")
                return None


def get_operation():  # function to request operation type from user

    # dictionary to contain operation symbol
    operation_dict = {"1" : "+", "2" : "-", "3" : "*", "4" : "/"}

    # loop to request operation type until options between 1-4 is selected
    while True:
        operation =  input("Choose an operation:\n1. Addition\n2. Subtraction\n3. Multiplication\n4. Division\n")
        if operation in operation_dict.keys():
            break

    # return tuple with operation number and symbol
    return int(operation), operation_dict[operation]


def main():
    # repeat = True
    # get first number into variable
    while True:
        first_number = get_number("first number")
        second_number = get_number("second number")

        operation, symbol = get_operation()

        result = execute(operation,first_number,second_number)

        print(f"Result: {first_number} {symbol} {second_number} = {result}")
        repeat_input = input("Would you like to perform another calulation? yes/y to continue, no/no to exit: ")

        if repeat_input.lower() == "no" or repeat_input.lower() == "n":
            print("Have a nice day")
            break
        else:
            continue




# call main function
if __name__ == "__main__":
    main()