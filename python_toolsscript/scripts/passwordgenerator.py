#!/usr/bin/env python
"""
A python script that generates random passwords.
both lowercase and large, numbers and characters
on request the complexity (number of characters and type of characters)
make use of flow control and functions!
"""

__author__ = "Timo Verbist"
__email__ = "timo.verbist@student.kdg.be"
__status__ = "Development"

import random, string

# declaration of the variables.
amount = 0
choice = 0


def main():  # main function with info text and invocation of the other functions.
    while True:
        print("We're going to generate a random password.")

        make_choice()
        # choice to quit
        if choice == 0:
            break

        get_length()

        return_password()


def make_choice():  # function that gives the options and lets the user choose.
    # global is used to get the same value of the variable in the different functions.
    global choice
    print("\noptions:")
    print("0) Go back to main menu")
    print("1) Only numbers")
    print("2) Only letters (small and big)")
    print("3) letters + other characters")
    print("4) combination of everything\n")
    # If the user gives something els than an int, (s)he'll get a message and start this function again.
    try:
        choice = int(input("give your choice (0-4):\n"))
    except:
        print("That's not a valid option!")
        make_choice()
    # if the user gives a number other than the options, (s)he'll get a message and start this function again
    if choice != 0 and choice != 1 and choice != 2 and choice != 3 and choice != 4:
        print("That's not a valid option!")
        make_choice()
    # print("")


def get_length():  # function to get the length of the password
    # global is used to get the same value of the variable in the different functions.
    global amount
    # If the user gives something els than an int, (s)he'll get a message and start this function again.
    try:
        amount = int(input("How many characters do you want in your password?\n"))
    except:
        print("That's not a valid input!\n")
        get_length()
    # print("password:")
    return amount


def return_password():  # function that prints out the password
    # This will check the input en print out the right kind of password.
    if choice == 1:
        for i in range(amount):
            print(random.randint(0, 9), end="")
    elif choice == 2:
        for i in range(amount):
            print(random.choice(string.ascii_letters), end="")
    elif choice == 3:
        for i in range(amount):
            print(random.choice(string.ascii_letters + "!@#$%^&*()_"), end="")
    elif choice == 4:
        for i in range(amount):
            print(random.choice(string.ascii_letters + string.digits + "!@#$%^&*()_"), end="")
    # else:
    #     print("That's not a valid input!\n")
    #     return_password()
    print("\n\n")


if __name__ == '__main__':  # code to execute if called from command-line
    main()
