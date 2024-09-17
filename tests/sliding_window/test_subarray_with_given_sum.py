"""
A file tests the find_subarray_with_given_sum function

Author: Nathan Lutala (nlutala)
"""

from dsa_problems.sliding_window.subarray_with_given_sum import (
    find_subarray_with_given_sum,
)


def test_find_subarray_with_given_sum_example_1():
    """
    Example 1:
    Input: arr = [15, 2, 4, 8, 9, 5, 10, 23], sum = 23
    Output: [2, 5]
    Explanation: Sum of elements between indices 2 and 5 is 2 + 4 + 8 + 9 = 23
    """
    arr = [15, 2, 4, 8, 9, 5, 10, 23]
    sum = 23
    assert find_subarray_with_given_sum(arr, sum) == [2, 5]


def test_find_subarray_with_given_sum_example_2():
    """
    Example 2:
    Input: arr = [1, 4, 0, 0, 3, 10, 5], sum = 7
    Output: [2, 5]
    Explanation: Sum of elements between indices 1 and 4 is 4 + 0 + 0 + 3 = 7
    """
    arr = [1, 4, 0, 0, 3, 10, 5]
    sum = 7
    assert find_subarray_with_given_sum(arr, sum) == [2, 5]


def test_find_subarray_with_given_sum_example_3():
    """
    Example 3:
    Input: arr = [1, 4], sum = 0
    Output: -1
    """
    arr = [1, 4]
    sum = 0
    assert find_subarray_with_given_sum(arr, sum) == -1
