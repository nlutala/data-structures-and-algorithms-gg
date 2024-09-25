"""
A file to tackle the coding interview question as found on the website below:
https://www.geeksforgeeks.org/sum-of-natural-numbers-using-recursion/

Author: Nathan Lutala (nlutala)
"""


def recur_sum(n: int) -> int:
    """
    Given a number n, find sum of first n natural numbers.\n

    :param - n (an integer)\n

    Return the sum of the first n numbers.
    """
    if n == 1:
        return n
    else:
        return n + recur_sum(n - 1)
