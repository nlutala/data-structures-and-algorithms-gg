"""
A file to tackle the coding interview question as found on the website below:
https://www.geeksforgeeks.org/program-to-print-first-n-fibonacci-numbers/

Author: Nathan Lutala (nlutala)
"""


def first_n_fibonacci(n: int) -> list[int]:
    """
    Given an integer N. The task is to find the first N Fibonacci numbers.\n

    :param - n (an integer)\n

    Returns the first n fibonacci numbers.
    """
    if n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    elif n > 2:
        return first_n_fibonacci(n - 1) + [
            first_n_fibonacci(n - 1)[-1] + first_n_fibonacci(n - 1)[-2]
        ]

    return []
