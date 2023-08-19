#Donald's Basic calculator
#this function adds two numbers
def add(x,y):
    return x + y

#this function subtracts two numbers
def subtract(x,y):
    return x-y

#this function multiplies two numbers
def multiply(x,y):
    return x * y

#this function divides two numbers
def divide(x,y):
    try:
        return x / y
    except ZeroDivisionError as e:
        return e

#this function provides the modulus of two numbers
def modulus(x,y):
    try:
        return x % y
    except ZeroDivisionError as e:
        return e


print('''Welcome!
Simple calculator
Select operation.''')
print('1.add')
print('2.subtract')
print('3.multiply')
print('4.divide')
print('5.modulus')

while True:
    #take input from the user
    choice = input('Enter choice(1/2/3/4/5):')
    
    #check if the choice is one of the five options
    if choice in ('1','2','3','4','5'):
        try:
            num1 = float(input('Enter first number:'))
            num2 = float(input('Enter second number'))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue
            
        if choice == '1':
            print(num1, '+', num2, '=', add(num1, num2))
        
        elif choice == '2':
            print (num1, '+', num2, '=', subtract(num1, num2))
            
        elif choice == '3':
            print (num1, '+', num2, '=', multiply(num1, num2))
            
        elif choice == '4':
            print (num1, '+', num2, '=', divide(num1, num2))
            
        elif choice == '5':
            print (num1, '+', num2, '=', modulus(num1, num2))
            
            
        #check if user wants another calculation
        # break the while loop if the answer is no
        next_calculation = input ("Let's do a different calculation?(yes/no):")
        if next_calculation == 'no':
          break
    else:
         print('invalid input')
