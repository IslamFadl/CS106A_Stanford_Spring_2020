"""
File: subtract_numbers.py
-------------------------
This program gets two real-values from the user and prints
the first number minus the second number.
"""


def main():
    """
    The user gets to define 2 numbers: num1 and num2.
    the result is evaluated from the subtraction of num2 from num1.
    the result is printed at the end of the program.
    """
    print("This program subtracts one number form another.")
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    result = num1 - num2
    print("The result is: " + str(result))

# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()
