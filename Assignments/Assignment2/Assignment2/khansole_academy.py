"""
File: khansole_academy.py
-------------------------
Add your comments here.
"""

import random


def main():
    correct_answers = 0
    while correct_answers != 3:
        num1 = random.randint(10, 99)
        num2 = random.randint(10, 99)
        print("What is " + str(num1) + " + " + str(num2) + " ?")
        sum = num1 + num2
        Your_answer = int(input("Your answer is: "))
        if sum == Your_answer:
            print("Correct! You've gotten " + str(correct_answers+1) + " correct in a row.")
            correct_answers += 1
        else:
            print("Incorrect. The expected answer is: " + str(sum))
            correct_answers = 0
    print("Congratulations! You mastered addition.")



# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()
