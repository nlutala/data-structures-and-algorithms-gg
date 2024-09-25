"""
A file to tackle the coding interview question as found on the website below:
https://www.geeksforgeeks.org/sum-digit-number-using-recursion/?

Author: Nathan Lutala (nlutala)
"""


def sum_digits(number: int) -> int:
    """
    Given a number, we need to find sum of its digits using recursion.\n

    :param - number (an integer)\n

    Return the sum of the digits of a number.
    """
    if len(str(number)) == 1:
        return number
    else:
        return int(str(number)[0]) + sum_digits(int((str(number)[1:])))
