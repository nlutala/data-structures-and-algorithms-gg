"""
A file test the fibonacci_numbers function

Author: Nathan Lutala (nlutala)
"""

from dsa_problems.recursion.level1.print_first_n_fibonacci_numbers import (
    fibonacci_numbers,
)


def test_fibonacci_numbers_example_1():
    """
    Example 1:
    Input: n = 3
    Output: 0 1 1
    """
    n = 3
    assert fibonacci_numbers(n) == [0, 1, 1]


def test_fibonacci_numbers_example_2():
    """
    Example 2:
    Input: n = 7
    Output: 0 1 1 2 3 5 8
    """
    n = 7
    assert fibonacci_numbers(n) == [0, 1, 1, 2, 3, 5, 8]


# My own custom test
def test_fibonacci_numbers_example_3():
    """
    Example 3:
    Input: n = 0
    Output: []
    """
    n = 0
    assert fibonacci_numbers(n) == []
