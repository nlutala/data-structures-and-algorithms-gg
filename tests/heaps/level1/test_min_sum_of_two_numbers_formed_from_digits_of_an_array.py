"""
A file tests the min_sum function

Author: Nathan Lutala (nlutala)
"""

from dsa_problems.heaps.level1.min_sum_of_two_numbers_formed_from_digits_of_an_array import (
    min_sum,
)


def test_min_sum_example_1():
    """
    Example 1:
    Input: [6, 8, 4, 5, 2, 3]
    Output: 604
    Explanation: The minimum sum is formed by numbers 358 and 246
    """
    arr = [6, 8, 4, 5, 2, 3]
    assert min_sum(arr) == 604


def test_min_sum_example_2():
    """
    Example 2:
    Input: [5, 3, 0, 7, 4]
    Output: 82
    Explanation: The minimum sum is formed by numbers 35 and 047
    """
    arr = [5, 3, 0, 7, 4]
    assert min_sum(arr) == 82
