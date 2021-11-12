# Calculator
# import packages
from art import logo
import os


# create four functions
# plus
def plus(number1, number2):
    return number1 + number2


# minus
def minus(number1, number2):
    return number1 - number2


# multiply
def multiply(number1, number2):
    return number1 * number2


# divide
def divide(number1, number2):
    return number1 / number2


# Generate a operation dictionary to call functions
operations = {
    "+": plus,
    "-": minus,
    "*": multiply,
    "/": divide
}


# create a function to do the operation
def calculate(operator, number1, number2):
    return operations[operator](number1, number2)


# create a function to start a new calculation
def start_calculation():
    # Greetings
    print(logo)

    end_of_calculation = False
    # gather input
    first_number = float(input("What's the first number?: "))
    for operation in operations:
        print(operation)

    # loop if continuing the calculation
    while not end_of_calculation:
        operation_symbol = input("Pick an operation: ")
        second_number = float(input("What's the next number?: "))
        result = calculate(operator=operation_symbol, number1=first_number, number2=second_number)
        print(f"{first_number} {operation_symbol} {second_number} = {result}")

        # continue the calculation or start a new one
        continue_calculation = input(
            f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ")
        if continue_calculation == 'y':
            first_number = result
        elif continue_calculation == 'n':
            end_of_calculation = True
            # clear the screen
            os.system('clear')
            # start a new calculation
            start_calculation()


# call the calculator function
start_calculation()
