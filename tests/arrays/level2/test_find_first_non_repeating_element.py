"""
A file tests the find_first_repeating_integer function

Author: Nathan Lutala (nlutala)
"""

from dsa_problems.arrays.level2.find_first_non_repeating_element import (
    find_non_repeating_integer,
)


def test_find_first_non_repeating_integer_example_1():
    """
    Example 1:
    Input: {-1, 2, -1, 3, 0}
    Output: 2
    Explanation: The first number that does not repeat is: 2
    """
    arr = [-1, 2, -1, 3, 0]

    assert find_non_repeating_integer(arr) == 2


def test_find_first_non_repeating_integer_example_2():
    """
    Example 2:
    Input: {9, 4, 9, 6, 7, 4}
    Output: 6
    """
    arr = [9, 4, 9, 6, 7, 4]

    assert find_non_repeating_integer(arr) == 6
