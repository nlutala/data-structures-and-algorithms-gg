"""
A file test the array_sum function

Author: Nathan Lutala (nlutala)
"""

from dsa_problems.recursion.level1.sum_of_array_using_recursion import array_sum


def test_array_sum_example_1():
    """
    Example 1:
    Input: arr[] = {1, 2, 3}
    Output: 6
    Explanation: 1 + 2 + 3 = 6
    """
    arr = [1, 2, 3]
    assert array_sum(arr) == 6


def test_array_sum_example_2():
    """
    Example 2:
    Input: arr[] = {15, 12, 13, 10}
    Output: 50
    """
    arr = [15, 12, 13, 10]
    assert array_sum(arr) == 50
