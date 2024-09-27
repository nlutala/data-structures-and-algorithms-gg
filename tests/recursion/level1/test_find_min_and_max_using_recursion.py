"""
A file test the get_min_and_max function

Author: Nathan Lutala (nlutala)
"""

from dsa_problems.recursion.level1.find_min_and_max_using_recursion import (
    get_min_and_max,
)


def test_get_min_and_max_example_1():
    """
    Example 1:
    Input: arr = {1, 4, 3, -5, -4, 8, 6};
    Output: min = -5, max = 8
    """
    arr = [1, 4, 3, -5, -4, 8, 6]
    assert get_min_and_max(arr, len(arr)) == [-5, 8]


def test_get_min_and_max_example_2():
    """
    Example 2:
    Input: arr = {1, 4, 45, 6, 10, -8};
    Output: min = -8, max = 45
    """
    arr = [1, 4, 45, 6, 10, -8]
    assert get_min_and_max(arr, len(arr)) == [-8, 45]
