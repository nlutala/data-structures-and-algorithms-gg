"""
A file tests the find_subarray_with_sum function

Author: Nathan Lutala (nlutala)
"""

from arrays.find_subarray_with_given_sum_from_array import find_subarray_with_sum


def test_find_subarray_with_sum_example_1():
    """
    Example 1:
    Input: arr[] = {15, 2, 4, 8, 9, 5, 10, 23}, sum = 26
    Output: 2 5
    Explanation: Sum of elements between indices 2 and 5 is 2 + 4 + 8 + 9 = 23
    """
    arr = [15, 2, 4, 8, 9, 5, 10, 23]
    s = 26

    assert find_subarray_with_sum(arr, s) == [2, 5]


def test_find_subarray_with_sum_example_2():
    """
    Example 2:
    Input: arr[] = {1, 4, 0, 0, 3, 10, 5}, sum = 7
    Output: 1 4
    Explanation: Sum of elements between indices 1 and 4 is 4 + 0 + 0 + 3 = 7
    """
    arr = [1, 4, 0, 0, 3, 10, 5]
    s = 7

    assert find_subarray_with_sum(arr, s) == [1, 4]


def test_find_subarray_with_sum_example_3():
    """
    Example 2:
    Input: arr[] = {1, 4}, sum = 0
    Output: -1
    Explanation: There is no subarray with 0 sum
    """
    arr = [1, 4]
    s = 0

    assert find_subarray_with_sum(arr, s) == [-1]
