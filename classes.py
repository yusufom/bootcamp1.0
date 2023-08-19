class SimpleCalculator:

    def __init__(self):
        self.trials = 5


    def operation(self, x, y, operation):
        try:
            if operation == 1:
                return x + y
            elif operation == 2:
                return x - y
            elif operation == 3:
                return x * y
            elif operation == 4:
                return x / y
        except ZeroDivisionError as e:
            return e
        
    def get_valid_operation(self, min=1, max=4):
        super(SimpleCalculator, self).get_valid_operation(min, max)
        for i in range(self.trials):
            try:
                operation = int(input("Choose an operation:\n1. Addition\n2. Subtraction\n3. Multiplication\n4. Division \nEnter the number corresponding to the operation: "))
                if min <= operation <= max:
                    return operation
                else:
                    print("Invalid operation. Please enter a valid choice.")
            except ValueError:
                print("Invalid input. Please enter a valid number.")
        # print("Max trials reached. Exiting......")
        return False

    def get_valid_number(self, prompt):
        for i in range(self.trials):
            try:
                number =  float(input(f"Enter the {prompt} number: "))
                return number
            except ValueError as e:
                self.trials -= 1
                print(f"Invalid input. Please enter a valid number. remaining trials {self.trials}")
        return False
            


    def main_operation(self):
        while True:
            num1 = self.get_valid_number("first")
            num2 = self.get_valid_number("second")
            operation = self.get_valid_operation()
            if isinstance(num1, float) and isinstance(num2, float):
                result = self.operation(num1, num2, operation)
                print(result)
                repeat_input = input("Would you like to perform another calulation? yes/y to continue, no/no to exit: ")

                if repeat_input.lower() == "no" or repeat_input.lower() == "n":
                    print("Have a nice day")
                    break
                else:
                    continue
            else:
                print("Max trials exceeded.")
                break
        
class ComplexCalculator(SimpleCalculator):

    def __init__(self):
        self.attempt = 4
        super().__init__()

    def operation(self, x, y, operation):
        super().operation(x, y, operation)
        try:
            if operation == 5:
                return x % y
        except ZeroDivisionError as e:
            return e
    
    def get_valid_operation(self, min=1, max=5):
        return super(SimpleCalculator, self).get_valid_operation(min, max)

calc = ComplexCalculator()
calc.main_operation()



