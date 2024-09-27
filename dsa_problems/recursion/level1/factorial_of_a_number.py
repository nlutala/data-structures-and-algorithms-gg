"""
A file to tackle the coding interview question as found on the website below:
https://www.geeksforgeeks.org/program-for-factorial-of-a-number/

Author: Nathan Lutala (nlutala)
"""


def factorial(number: int) -> int:
    """
    Given the number n (n >=0), find its factorial. Factorial of n is defined as
    1 x 2 x … x n. For n = 0, factorial is 1.\n

    :param - number (a positive integer)\n

    Return the factorial of a positive integer.
    """

    """
    if number <= 1:
        return 1
    else:
        return number * factorial(number - 1)
    """

    # A better solution (accounts for negative numbers and decimal/floating point
    # numbers)
    if number < 0 or str(type(number)) != "<class 'int'>":
        raise ArithmeticError()
    elif number <= 1:
        return 1

    return number * factorial(number - 1)
