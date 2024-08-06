"""
A file tests the find_kth_smallest_element function

Author: Nathan Lutala (nlutala)
"""

from arrays.kth_smallest_element_in_unsorted_array import find_kth_smallest_element


def test_find_kth_smallest_element_example_1():
    """
    Example 1:
    Input: arr[] = {7, 10, 4, 3, 20, 15}, K = 3
    Output: 10
    """
    arr = [7, 10, 4, 3, 20, 15]
    k = 3

    assert find_kth_smallest_element(arr, k) == 7


def test_find_kth_smallest_element_example_2():
    """
    Example 2:
    Input: arr[] = {7, 10, 4, 3, 20, 15}, K = 4
    Output: 10
    """
    arr = [7, 10, 4, 3, 20, 15]
    k = 4

    assert find_kth_smallest_element(arr, k) == 10
