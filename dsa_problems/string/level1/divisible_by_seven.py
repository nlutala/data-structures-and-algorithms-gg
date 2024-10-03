"""
A file to tackle the coding interview question as found on the website below:
https://www.geeksforgeeks.org/divisibility-by-7/

Author: Nathan Lutala (nlutala)
"""


def is_divisble_by_7(n: int) -> bool:
    """
    Given a number N, the task is to check if it is divisible by 7 or not.\n
    Note: You are not allowed to use the modulo operator, floating point arithmetic is
    also not allowed.\n

    :param - n (an integer)\n

    Returns true if the number is divisible by 7. False if otherwise.
    """
    n = abs(n)

    if n == 0:
        return True

    while n > 0:
        n -= 7

        if n == 0:
            return True

    return False
