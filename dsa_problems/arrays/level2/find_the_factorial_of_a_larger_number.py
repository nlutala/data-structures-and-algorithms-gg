"""
A file to tackle the coding interview question as found on the website below:
https://www.geeksforgeeks.org/factorial-large-number/

Author: Nathan Lutala (nlutala)
"""


def find_factorial(n: int) -> int:
    """
    Factorial of a non-negative integer, is the multiplication of all integers
    smaller than or equal to n.\n

    :param - n (int)\n

    returns the factorial of a large number
    """
    if n > 1:
        return n * find_factorial(n - 1)

    return n * 1
