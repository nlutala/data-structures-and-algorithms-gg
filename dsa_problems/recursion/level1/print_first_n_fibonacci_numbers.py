"""
A file to tackle the coding interview question as found on the website below:
https://www.geeksforgeeks.org/program-to-print-first-n-fibonacci-numbers/

Author: Nathan Lutala (nlutala)
"""


def fibonacci_numbers(n: int) -> list[int]:
    """
    Given an integer N. The task is to find the first N Fibonacci numbers.\n

    :param - n (an integer)\n

    Return the first n numbers of the fibonnaci sequence.
    """
    # Not sure how to do this
    # Here's the geeksforgeeks solution
    """
    if num == 0:
        return 0
    elif num == 1:
        return 1
    else:
        # printing fibonacci numbers
        return fibonacci_numbers(num-2)+fibonacci_numbers(num-1)
    """

    # I disagree with the above as if 0 is passed as a parameter, no values
    # should be returned.
    # Here are my ammendments

    if n == 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        return fibonacci_numbers(n-1) + [
            fibonacci_numbers(n-1)[-2] + fibonacci_numbers(n-1)[-1]
        ]
