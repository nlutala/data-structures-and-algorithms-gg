"""
A file to tackle the coding interview question as found on the website below:
https://www.geeksforgeeks.org/recursive-function-check-string-palindrome/

Author: Nathan Lutala (nlutala)
"""


def is_palindrome(string: str) -> bool:
    """
    Given the number n (n >=0), find its factorial. Factorial of n is defined as
    1 x 2 x … x n. For n = 0, factorial is 1.\n

    :param - number (a positive integer)\n

    Return the factorial of a positive integer.
    """
    if len(string) == 1:
        return True
    else:
        if string[0] == string[-1]:
            return is_palindrome(string[1 : len(string) - 1])

        return False
