"""
A file tests the find_missing_number function

Author: Nathan Lutala (nlutala)
"""

from dsa_problems.arrays.level2.find_the_missing_number import (
    find_missing_number,
)


def test_find_missing_number_example_1():
    """
    Example 1:
    Input: arr[] = {1, 2, 4, 6, 3, 7, 8} , N = 8
    Output: 5
    Explanation: Here the size of the array is 8, so the range will be [1, 8].
    The missing number between 1 to 8 is 5
    """
    arr = [1, 2, 4, 6, 3, 7, 8]

    assert find_missing_number(arr) == 5


def test_find_missing_number_example_2():
    """
    Example 1:
    Input: arr[] = {1, 2, 3, 5}, N = 5
    Output: 4
    Explanation: Here the size of the array is 4, so the range will be [1, 5].
    The missing number between 1 to 5 is 4
    """
    arr = [1, 2, 3, 5]

    assert find_missing_number(arr) == 4
