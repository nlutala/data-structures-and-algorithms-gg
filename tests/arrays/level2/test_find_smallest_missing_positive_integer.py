"""
A file tests the smallest_missing_positive_int function

Author: Nathan Lutala (nlutala)
"""

from dsa_problems.arrays.level2.find_smallest_missing_positive_integer import (
    smallest_missing_positive_int,
)


def test_smallest_missing_positive_int_example_1():
    """
    Example 1:
    Input:  arr[] = {2, 3, 7, 6, 8, -1, -10, 15}
    Output: 1
    """
    arr = [2, 3, 7, 6, 8, -1, -10, 15]
    assert smallest_missing_positive_int(arr) == 1


def test_smallest_missing_positive_int_example_2():
    """
    Example 2:
    Input:  arr[] = { 2, 3, -7, 6, 8, 1, -10, 15 }
    Output: 4
    """
    arr = [2, 3, -7, 6, 8, 1, -10, 15]
    assert smallest_missing_positive_int(arr) == 4


def test_smallest_missing_positive_int_example_3():
    """
    Example 3:
    Input: arr[] = {1, 1, 0, -1, -2}
    Output: 2
    """
    arr = [1, 5, 7, -1]
    assert smallest_missing_positive_int(arr) == 2
