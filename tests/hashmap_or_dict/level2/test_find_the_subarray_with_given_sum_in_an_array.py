"""
A file tests the get_subarray_with_given_sum function

Author: Nathan Lutala (nlutala)
"""

from dsa_problems.hashmap_or_dict.level2.find_the_subarray_with_given_sum_in_an_array import (
    get_subarray_with_given_sum,
)


def test_get_subarray_with_given_sum_example_1():
    """
    Example 1
    Input: arr[] = {15, 2, 4, 8, 9, 5, 10, 23}, sum = 23
    Output: 2 5
    Explanation: Sum of elements between indices 2 and 5 is 2 + 4 + 8 + 9 = 23
    """
    arr, s = [15, 2, 4, 8, 9, 5, 10, 23], 23
    assert get_subarray_with_given_sum(arr, s) == (2, 5)


def test_get_subarray_with_given_sum_example_2():
    """
    Example 2
    Input: arr[] = {1, 4, 0, 0, 3, 10, 5}, sum = 7
    Output: 2 5
    Explanation: Sum of elements between indices 2 and 5 is 4 + 0 + 0 + 3 = 7
    """
    arr, s = [1, 4, 0, 0, 3, 10, 5], 7
    assert get_subarray_with_given_sum(arr, s) == (2, 5)


def test_get_subarray_with_given_sum_example_3():
    """
    Example 3
    Input: arr[] = {1, 4}, sum = 0
    Output: -1
    Explanation: There is no subarray with 0 sum
    """
    arr, s = [1, 4], 0
    assert get_subarray_with_given_sum(arr, s) == -1
