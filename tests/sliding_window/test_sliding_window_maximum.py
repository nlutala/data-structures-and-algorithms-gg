"""
A file tests the max_of_subarray function

Author: Nathan Lutala (nlutala)
"""

from dsa_problems.sliding_window.sliding_window_maximum import max_of_subarray


def test_max_of_subarray_example_1():
    """
    Example 1:
    Input: arr[] = {1, 2, 3, 1, 4, 5}, K = 3
    Output: 3 3 4 5
    Explanation: Maximum of 1, 2, 3 is 3
                 Maximum of 2, 3, 1 is 3
                 Maximum of 3, 1, 4 is 4
                 Maximum of 1, 4, 5 is 5
    """
    arr = [1, 2, 3, 1, 4, 5]
    k = 3
    assert max_of_subarray(arr, k) == [3, 3, 4, 5]


def test_max_of_subarray_example_2():
    """
    Example 2:
    Input: arr[] = {8, 5, 10, 7, 9, 4, 15, 12, 90, 13}, K = 4
    Output: 10 10 10 15 15 90 90
    Explanation: Maximum of first 4 elements is 10, similarly for next 4
                 elements (i.e from index 1 to 4) is 10, So the sequence
                 generated is 10 10 10 15 15 90 90
    """
    arr = [8, 5, 10, 7, 9, 4, 15, 12, 90, 13]
    k = 4
    assert max_of_subarray(arr, k) == [10, 10, 10, 15, 15, 90, 90]


def test_max_of_subarray_example_3():
    """
    Example 3:
    Input: arr[] = {20, 10, 30}, K = 1
    Output: 20 10 30
    """
    arr = [20, 10, 30]
    k = 1
    assert max_of_subarray(arr, k) == [20, 10, 30]
