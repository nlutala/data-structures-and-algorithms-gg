"""
A file test the first_n_fibonacci function

Author: Nathan Lutala (nlutala)
"""

from dsa_problems.recursion.level1.program_to_print_first_n_fibonacci_numbers import (
    first_n_fibonacci,
)


def test_first_n_fibonacci_example_1():
    """
    Example 1:
    Input: n = 3
    Output: 0 1 1
    """
    assert first_n_fibonacci(3) == [0, 1, 1]


def test_first_n_fibonacci_example_2():
    """
    Example 2:
    Input: n = 7
    Output: 0 1 1 2 3 5 8
    """
    assert first_n_fibonacci(7) == [0, 1, 1, 2, 3, 5, 8]


# Custom tests
def test_first_n_fibonacci_example_3():
    """
    Example 3:
    Input: n = 10
    Output: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
    """
    assert first_n_fibonacci(10) == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]


def test_first_n_fibonacci_example_4():
    """
    Example 4:
    Input: n = 1
    Output: [0]
    """
    assert first_n_fibonacci(1) == [0]


def test_first_n_fibonacci_example_5():
    """
    Example 5:
    Input: n = 0
    Output: []
    """
    assert first_n_fibonacci(0) == []
