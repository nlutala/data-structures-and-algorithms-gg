"""
A file test the sum_digits function

Author: Nathan Lutala (nlutala)
"""

from dsa_problems.recursion.level1.sum_of_number_digits_using_recusion import (
    sum_digits,
)


def test_sum_digits_example_1():
    """
    Example 1:
    Input: 12345
    Output: 15
    """
    assert sum_digits(12345) == 15


def test_sum_digits_example_2():
    """
    Example 2:
    Input: 45632
    Output: 20
    """
    assert sum_digits(45632) == 20
