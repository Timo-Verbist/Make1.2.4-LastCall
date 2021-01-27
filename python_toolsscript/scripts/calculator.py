#!/usr/bin/env python
"""
A re-make of your calculator that conforms to flow control.
You ask the user for 2 numbers
You ask the user to enter an operation
You give correct output
Your custom calculator now fully customized / improved with the right imports, functions and flow control.
"""

__author__ = "Timo Verbist"
__email__ = "timo.verbist@student.kdg.be"
__status__ = "finished"


def main():
    print("We're going to multiplicate, divide, add or subtract two numbers") # information text

# loop
    while True:
        # let the user choose an operator.
        sign = str(input('Choose multiplication(*), division(/), addition(+) or subtraction(-)   (q: go back to main '
                         'menu)\n'))
        # If the user gives an input other than the previous given ones, he'll get a message and start over again.
        if sign != "*" and sign != "/" and sign != "+" and sign != "-" and sign != "q":
            print("not a valid sign!\n")
            main()
        elif sign == "q":
            break

        # If the user doesn't give a natural number, he'll get a message and start over again. (same with number2)
        try:
            number1 = int(input('Give number1\n'))
        except:
            print("this is not a natural number!\n")
            main()

        try:
            number2 = int(input('Give number2\n'))
        except:
            print("this is not a natural number!\n")
            main()

        # this wil check the input, carry out the right calculation and print out the output.
        if sign == "*":
            outcome = multiplication(number1, number2)
        elif sign == "/":
            outcome = division(number1, number2)
        elif sign == "+":
            outcome = addition(number1, number2)
        elif sign == "-":
            outcome = subtraction(number1, number2)
        # elif sign == "q":
        #     break
        # print("The outcome is", outcome, "\n")


# functions:


def multiplication(number1, number2):
    return number1 * number2


def division(number1, number2):
    return number1 / number2


def addition(number1, number2):
    return number1 + number2


def subtraction(number1, number2):
    return number1 - number2


if __name__ == '__main__':  # runs the main function in the script "calculator.py"
    main()
