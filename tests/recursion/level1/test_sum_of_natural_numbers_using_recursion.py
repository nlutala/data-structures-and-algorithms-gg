"""
A file test the recur_sum function

Author: Nathan Lutala (nlutala)
"""

from dsa_problems.recursion.sum_of_natural_numbers_using_recursion import recur_sum


def test_recur_sum_example_1():
    """
    Example 1:
    Input : 3
    Output : 6
    Explanation : 1 + 2 + 3 = 6
    """
    n = 3
    assert recur_sum(n) == 6


def test_recur_sum_example_2():
    """
    Example 1:
    Input : 5
    Output : 15
    Explanation : 1 + 2 + 3 + 4 + 5 = 15
    """
    n = 5
    assert recur_sum(n) == 15
