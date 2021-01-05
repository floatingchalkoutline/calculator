from art import logo
from operations import Calculator

calculator = Calculator()
operations = calculator.OPERATIONS
is_on = True

print(logo)
operand_one = int(input("What's the first number?: "))
while is_on:
    for symbol in operations:
        print(symbol)
    operation = input(f"Pick an operation: ")
    if operation == "**":
        operand_two = 0
    else:
        operand_two = int(input("What's the second number?: "))
    answer = calculator.calculate(operand_one, operand_two, operation)
    print(answer)
    keep_calculating = input(f"Continue calculating with {answer}? Type 'y' or 'n': ")
    if keep_calculating == "y":
        if answer == None:
            operand_one = 0
        else:
            operand_one = answer
    else:
        is_on = False


