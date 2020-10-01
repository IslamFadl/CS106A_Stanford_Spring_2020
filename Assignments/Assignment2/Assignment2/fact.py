MAX_NUM = 4

def factorial(n):
    '''
    This function returns factorial of n (denoted n!)
    Input: n (number to compute factorial of)
    Return: value of factorial
    Doctests:
    >>> factorial(3)
    6
    >>> factorial(2)
    2
    >>> factorial(1)
    1
    '''
    result =1
    for i in range(1, n+1):
        result *= i
    return result

def main():
    '''
    Prints factorials for all numbers form 0 to MAX_NUM
    '''
    for i in range(MAX_NUM):
        print(i, factorial(i))


# This line is required at the end of a python file
# to call the main() function.
if __name__ == '__main__':
    main()